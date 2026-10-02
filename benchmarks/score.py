#!/usr/bin/env python3
"""Aggregate explicit reviewer judgments; never grade answers by keyword overlap."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


DIMENSIONS = (
    "conclusion", "source_fidelity", "attribution", "minhag_and_scope",
    "uncertainty", "usefulness",
)
RESULT_LABEL = "development rubric agreement, not validated halakhic accuracy"
HEX_DIGEST = re.compile(r"[0-9a-fA-F]{64}\Z")


class ScoringError(Exception):
    """The judgments or their response provenance cannot be assessed."""


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ScoringError(f"Could not read JSON from {path.name}: {error}") from error


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def validate_cases(document):
    if (
        not isinstance(document, dict)
        or type(document.get("schema_version")) is not int
        or document["schema_version"] != 1
        or not isinstance(document.get("cases"), list)
        or not document["cases"]
    ):
        raise ScoringError("Cases must be a schema_version=1 object with a nonempty cases list.")
    cases = document["cases"]
    seen = set()
    for case in cases:
        if not isinstance(case, dict) or not nonempty_string(case.get("id")) or not nonempty_string(case.get("prompt")):
            raise ScoringError("Each case needs a nonempty id and prompt.")
        if case["id"] in seen:
            raise ScoringError(f"Duplicate suite case ID: {case['id']}")
        seen.add(case["id"])
    return cases


def validate_run(run):
    if not isinstance(run, dict):
        raise ScoringError("A run metadata object is required.")
    for field in ("label", "model", "host", "reviewer", "retrieval_mode"):
        if not nonempty_string(run.get(field)):
            raise ScoringError(f"run.{field} must be a nonempty string.")
    if not isinstance(run.get("skill_sha256"), str) or not HEX_DIGEST.fullmatch(run["skill_sha256"]):
        raise ScoringError("run.skill_sha256 must be a SHA-256 hexadecimal digest.")
    if run.get("reviewer_type") not in ("ai", "human", "expert"):
        raise ScoringError("run.reviewer_type must be ai, human, or expert.")
    if not isinstance(run.get("notes"), str):
        raise ScoringError("run.notes must be a string; disclose relevant evaluation limitations.")


def response_digest(filename, base_dir):
    if not nonempty_string(filename):
        raise ScoringError("response_file must be a nonempty relative path.")
    relative = Path(filename)
    if relative.is_absolute() or ".." in relative.parts:
        raise ScoringError("response_file must remain inside the judgments directory.")
    try:
        root = base_dir.resolve(strict=True)
        path = (root / relative).resolve(strict=True)
        path.relative_to(root)
    except (OSError, ValueError) as error:
        raise ScoringError("response_file is missing or escapes the judgments directory.") from error
    try:
        digest = hashlib.sha256()
        with path.open("rb") as response:
            for chunk in iter(lambda: response.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError as error:
        raise ScoringError(f"Cannot read response_file {filename!r}.") from error


def score_judgments(document, cases, base_dir):
    if not isinstance(document, dict):
        raise ScoringError("Judgments must be an object containing run and judgments.")
    validate_run(document.get("run"))
    judgments = document.get("judgments")
    if not isinstance(judgments, list):
        raise ScoringError("judgments must be a list.")
    case_ids = [case["id"] for case in cases]
    known = set(case_ids)
    seen = set()
    assessed = []
    totals = {dimension: 0 for dimension in DIMENSIONS}
    for judgment in judgments:
        if not isinstance(judgment, dict) or not nonempty_string(judgment.get("case_id")):
            raise ScoringError("Each judgment needs a nonempty case_id.")
        case_id = judgment["case_id"]
        if case_id not in known:
            raise ScoringError(f"Unknown case ID: {case_id}")
        if case_id in seen:
            raise ScoringError(f"Duplicate judgment for case ID: {case_id}")
        seen.add(case_id)
        scores = judgment.get("scores")
        if not isinstance(scores, dict) or set(scores) != set(DIMENSIONS):
            raise ScoringError(f"{case_id}: scores must contain exactly the six rubric dimensions.")
        for dimension, value in scores.items():
            if type(value) is not int or value not in (0, 1, 2):
                raise ScoringError(f"{case_id}: {dimension} must be an integer 0, 1, or 2; booleans are invalid.")
        critical = judgment.get("critical_failure")
        if type(critical) is not bool:
            raise ScoringError(f"{case_id}: critical_failure must be a boolean.")
        if not nonempty_string(judgment.get("rationale")):
            raise ScoringError(f"{case_id}: a nonempty reviewer rationale is required.")
        expected_hash = judgment.get("response_sha256")
        if not isinstance(expected_hash, str) or not HEX_DIGEST.fullmatch(expected_hash):
            raise ScoringError(f"{case_id}: response_sha256 must be a SHA-256 hexadecimal digest.")
        actual_hash = response_digest(judgment.get("response_file"), base_dir)
        if actual_hash != expected_hash.lower():
            raise ScoringError(f"{case_id}: response_sha256 does not match the saved response; review the changed file again.")
        points = sum(scores.values())
        passes = not critical and points >= 10 and all(value >= 1 for value in scores.values())
        for dimension, value in scores.items():
            totals[dimension] += value
        assessed.append({
            "case_id": case_id,
            "response_file": judgment["response_file"],
            "response_sha256": actual_hash,
            "scores": scores,
            "points": points,
            "possible_points": 12,
            "critical_failure": critical,
            "passes": passes,
            "rationale": judgment["rationale"],
        })
    passing = [item["case_id"] for item in assessed if item["passes"]]
    return {
        "result_label": RESULT_LABEL,
        "run": document["run"],
        "reviewer_note": "Reviewer type, including expert, is self-attested and is not certification.",
        "assessment_method": "Explicit reviewer judgments; this script validates saved response hashes and aggregates scores, without evaluating answer meaning or independently verifying run metadata.",
        "assessed_count": len(assessed),
        "total_suite": len(cases),
        "rubric_points": sum(totals.values()),
        "possible_points": 12 * len(assessed),
        "dimension_points": totals,
        "dimension_possible_points": 2 * len(assessed),
        "critical_failures": [item["case_id"] for item in assessed if item["critical_failure"]],
        "passing_cases": passing,
        "passing_count": len(passing),
        "pass_rule": "Every dimension >=1, total >=10/12, and no critical failure.",
        "unassessed": [case_id for case_id in case_ids if case_id not in seen],
        "coverage_note": "Rubric totals describe assessed cases only. Unassessed cases are neither passes nor failures.",
        "assessments": assessed,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("judgments", type=Path, nargs="?", help="JSON containing run metadata and explicit reviewer judgments")
    parser.add_argument("--cases", type=Path, default=Path(__file__).with_name("cases.json"))
    parser.add_argument("--output", type=Path, help="Write JSON here instead of standard output")
    parser.add_argument("--questions", action="store_true", help="Emit only case IDs and prompts for blind task copies")
    args = parser.parse_args(argv)
    if args.questions and args.judgments is not None:
        parser.error("--questions does not accept a judgments file")
    if not args.questions and args.judgments is None:
        parser.error("provide a judgments file, or use --questions")
    try:
        cases = validate_cases(read_json(args.cases))
        if args.questions:
            report = [{"id": case["id"], "prompt": case["prompt"]} for case in cases]
        else:
            report = score_judgments(read_json(args.judgments), cases, args.judgments.parent)
        serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(serialized, encoding="utf-8")
        else:
            sys.stdout.write(serialized)
        return 0
    except (ScoringError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
