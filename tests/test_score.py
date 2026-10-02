"""Offline checks for scoring integrity, not halakhic answer quality."""

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "benchmarks" / "score.py"
SPEC = importlib.util.spec_from_file_location("score", SCRIPT)
score = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score)


class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.answer = self.root / "response.txt"
        self.answer.write_text("Synthetic candidate response.\n", encoding="utf-8")
        self.cases = [{"id": "a", "prompt": "Question A"}, {"id": "b", "prompt": "Question B"}]

    def document(self):
        return {
            "run": {
                "label": "Fixture only", "model": "fixture", "host": "unittest",
                "skill_sha256": "a" * 64, "reviewer": "Synthetic fixture",
                "reviewer_type": "ai", "retrieval_mode": "offline fixture", "notes": "Not a real evaluation.",
            },
            "judgments": [{
                "case_id": "a", "response_file": "response.txt",
                "response_sha256": hashlib.sha256(self.answer.read_bytes()).hexdigest(),
                "scores": {dimension: 2 for dimension in score.DIMENSIONS},
                "critical_failure": False,
                "rationale": "Synthetic reviewer rationale used only to exercise aggregation.",
            }],
        }

    def report(self, document):
        return score.score_judgments(document, self.cases, self.root)

    def test_partial_reporting_keeps_full_suite_denominator_visible(self):
        report = self.report(self.document())
        self.assertEqual(report["assessed_count"], 1)
        self.assertEqual(report["total_suite"], 2)
        self.assertEqual(report["rubric_points"], 12)
        self.assertEqual(report["possible_points"], 12)
        self.assertEqual(report["passing_cases"], ["a"])
        self.assertEqual(report["unassessed"], ["b"])
        self.assertEqual(report["result_label"], "development rubric agreement, not validated halakhic accuracy")

    def test_empty_judgments_are_zero_coverage(self):
        document = self.document()
        document["judgments"] = []
        report = self.report(document)
        self.assertEqual(report["possible_points"], 0)
        self.assertEqual(report["assessed_count"], 0)
        self.assertEqual(report["unassessed"], ["a", "b"])

    def test_duplicate_and_unknown_judgments_are_rejected(self):
        document = self.document()
        document["judgments"].append(document["judgments"][0].copy())
        with self.assertRaisesRegex(score.ScoringError, "Duplicate judgment"):
            self.report(document)
        document = self.document()
        document["judgments"][0]["case_id"] = "unknown"
        with self.assertRaisesRegex(score.ScoringError, "Unknown case"):
            self.report(document)

    def test_missing_dimension_is_rejected(self):
        document = self.document()
        del document["judgments"][0]["scores"]["conclusion"]
        with self.assertRaisesRegex(score.ScoringError, "six rubric dimensions"):
            self.report(document)

    def test_boolean_noninteger_and_out_of_range_scores_are_rejected(self):
        for value in (True, False, 1.0, "2", -1, 3):
            with self.subTest(value=value):
                document = self.document()
                document["judgments"][0]["scores"]["conclusion"] = value
                with self.assertRaises(score.ScoringError):
                    self.report(document)

    def test_missing_rationale_and_nonboolean_critical_flag_are_rejected(self):
        for key, value in (("rationale", "   "), ("critical_failure", 0)):
            with self.subTest(key=key):
                document = self.document()
                document["judgments"][0][key] = value
                with self.assertRaises(score.ScoringError):
                    self.report(document)

    def test_critical_failure_overrides_perfect_points(self):
        document = self.document()
        document["judgments"][0]["critical_failure"] = True
        report = self.report(document)
        self.assertEqual(report["rubric_points"], 12)
        self.assertEqual(report["critical_failures"], ["a"])
        self.assertEqual(report["passing_cases"], [])

    def test_zero_dimension_overrides_total_of_ten(self):
        document = self.document()
        document["judgments"][0]["scores"]["source_fidelity"] = 0
        report = self.report(document)
        self.assertEqual(report["rubric_points"], 10)
        self.assertEqual(report["passing_cases"], [])

    def test_ten_points_with_every_dimension_positive_passes(self):
        document = self.document()
        document["judgments"][0]["scores"]["conclusion"] = 1
        document["judgments"][0]["scores"]["usefulness"] = 1
        self.assertEqual(self.report(document)["passing_cases"], ["a"])

    def test_tampered_response_hash_is_rejected(self):
        document = self.document()
        self.answer.write_text("Changed after review.", encoding="utf-8")
        with self.assertRaisesRegex(score.ScoringError, "does not match"):
            self.report(document)

    def test_paths_cannot_escape_judgments_directory(self):
        for filename in ("../response.txt", str(self.answer.resolve())):
            with self.subTest(filename=filename):
                document = self.document()
                document["judgments"][0]["response_file"] = filename
                with self.assertRaisesRegex(score.ScoringError, "inside the judgments directory"):
                    self.report(document)
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other) / "outside.txt"
            outside.write_bytes(self.answer.read_bytes())
            (self.root / "link.txt").symlink_to(outside)
            document = self.document()
            document["judgments"][0]["response_file"] = "link.txt"
            with self.assertRaisesRegex(score.ScoringError, "escapes"):
                self.report(document)

    def test_expert_reviewer_label_remains_self_attested(self):
        document = self.document()
        document["run"]["reviewer_type"] = "expert"
        self.assertIn("self-attested", self.report(document)["reviewer_note"])

    def test_questions_mode_excludes_answer_key(self):
        cases_path = self.root / "cases.json"
        cases_path.write_text(json.dumps({"schema_version": 1, "cases": [
            {"id": "a", "prompt": "Question A", "answer_key": "Must remain hidden"}
        ]}), encoding="utf-8")
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = score.main(["--cases", str(cases_path), "--questions"])
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(stdout.getvalue()), [{"id": "a", "prompt": "Question A"}])

    def test_suite_schema_and_duplicate_ids_are_rejected(self):
        for document in (self.cases, {"schema_version": True, "cases": self.cases}, {"schema_version": 1, "cases": [self.cases[0], self.cases[0]]}):
            with self.subTest(document=document):
                with self.assertRaises(score.ScoringError):
                    score.validate_cases(document)


if __name__ == "__main__":
    unittest.main()
