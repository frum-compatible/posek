"""Offline contract tests; fixture prose is synthetic, never a quoted source."""

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse


SCRIPT = Path(__file__).parents[1] / "skills" / "posek" / "scripts" / "fetch_source.py"
SPEC = importlib.util.spec_from_file_location("fetch_source", SCRIPT)
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)
REF = "Shulchan Arukh, Orach Chayim 328:2"


def fixture():
    return {
        "ref": REF,
        "sections": ["328", "2"],
        "toSections": ["328", "2"],
        "textDepth": 2,
        "isSpanning": False,
        "warnings": [],
        "versions": [
            {
                "versionTitle": "Synthetic Hebrew fixture",
                "versionSource": "https://example.invalid/source",
                "license": "Public Domain",
                "language": "he",
                "isSource": True,
                "text": '<b>מקור</b><i data-commentator="Fixture" data-order="1"></i>',
            },
            {
                "versionTitle": "Synthetic English fixture",
                "versionSource": "https://example.invalid/translation",
                "license": "CC0",
                "language": "en",
                "isSource": False,
                "text": 'Synthetic text <small>[editorial note]</small>.',
            },
        ],
    }


def evidence(payload, requested=REF):
    raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    return source.build_evidence(requested, raw, source.source_url(requested))


def response(raw):
    result = Mock()
    result.__enter__ = Mock(return_value=result)
    result.__exit__ = Mock(return_value=False)
    result.read.return_value = raw
    return result


class EvidenceTests(unittest.TestCase):
    def test_markup_metadata_and_original_payload_digest_are_preserved(self):
        payload = fixture()
        raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        result = source.build_evidence(REF, raw, source.source_url(REF))
        for original, saved in zip(payload["versions"], result["versions"]):
            for key, value in original.items():
                self.assertEqual(saved[key], value)
        self.assertEqual(result["payload_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(result["canonical_ref"], REF)
        self.assertTrue(result["retrieved_at"].endswith("Z"))
        self.assertIn("does not verify", result["evidence_scope"])

    def test_nested_text_segmentation_is_not_flattened(self):
        payload = fixture()
        payload["versions"][0]["text"] = [["א", "ב"], ["ג"]]
        self.assertEqual(evidence(payload)["versions"][0]["text"], [["א", "ב"], ["ג"]])

    def test_chapter_and_ranges_are_rejected(self):
        for sections, to_sections in [(["328"], ["328"]), (["328", "2"], ["328", "3"])]:
            with self.subTest(sections=sections, to_sections=to_sections):
                payload = fixture()
                payload["sections"] = sections
                payload["toSections"] = to_sections
                with self.assertRaisesRegex(source.SourceError, "One exact segment"):
                    evidence(payload)

    def test_silently_changed_reference_is_rejected(self):
        with self.assertRaisesRegex(source.SourceError, "changed to"):
            evidence(fixture(), requested="Shulchan Arukh, Orach Chayim")

    def test_missing_reference_shape_fails_closed(self):
        payload = fixture()
        del payload["textDepth"]
        with self.assertRaises(source.SourceError):
            evidence(payload)

    def test_api_error_or_non_json_never_produces_evidence(self):
        with self.assertRaisesRegex(source.SourceError, "rejected"):
            evidence({"error": "Could not find title in reference"})
        with self.assertRaisesRegex(source.SourceError, "invalid JSON"):
            source.build_evidence(REF, b"<html>unavailable</html>", source.source_url(REF))

    def test_missing_or_partial_source_is_not_replaced_by_translation(self):
        for missing in ("", [], '<i data-commentator="Fixture"></i>', ["א", ""]):
            with self.subTest(missing=missing):
                payload = fixture()
                payload["versions"][0]["text"] = missing
                with self.assertRaisesRegex(source.SourceError, "original-language source"):
                    evidence(payload)

    def test_translation_alone_is_not_source_evidence(self):
        payload = fixture()
        payload["versions"] = payload["versions"][1:]
        with self.assertRaisesRegex(source.SourceError, "original-language source"):
            evidence(payload)

    def test_missing_english_is_retained_and_explicitly_warned(self):
        payload = fixture()
        payload["versions"][1]["text"] = ""
        result = evidence(payload)
        self.assertEqual(result["versions"][1]["text"], "")
        self.assertEqual(result["versions"][1]["text_status"], "missing")
        self.assertTrue(any("English text is unavailable" in warning for warning in result["warnings"]))

    def test_api_warnings_are_preserved(self):
        payload = fixture()
        warning = {"english": "Synthetic API warning"}
        payload["warnings"] = [warning]
        self.assertIn(warning, evidence(payload)["warnings"])

    def test_request_disables_replacement_and_preserves_editorial_markup(self):
        url = source.source_url(REF)
        query = parse_qs(urlparse(url).query)
        self.assertEqual(query["version"], ["source", "english"])
        self.assertEqual(query["fill_in_missing_segments"], ["0"])
        self.assertEqual(query["return_format"], ["default"])
        self.assertIn("%3A2", url)


class DownloadTests(unittest.TestCase):
    def test_response_is_capped_and_timeout_is_bounded(self):
        network_response = response(b"x" * (source.MAX_BYTES + 1))
        opener = Mock()
        opener.open.return_value = network_response
        with patch.object(source, "build_opener", return_value=opener):
            with self.assertRaisesRegex(source.SourceError, "exceeded 2 MiB"):
                source.download(source.source_url(REF))
        network_response.read.assert_called_once_with(source.MAX_BYTES + 1)
        self.assertLessEqual(opener.open.call_args.kwargs["timeout"], 20)

    def test_transient_http_errors_have_at_most_two_retries(self):
        for status in (429, 503):
            with self.subTest(status=status):
                opener = Mock()
                opener.open.side_effect = [HTTPError("url", status, "Error", {}, None) for _ in range(3)]
                with patch.object(source, "build_opener", return_value=opener), patch.object(source.time, "sleep") as sleep:
                    with self.assertRaises(source.SourceError):
                        source.download(source.source_url(REF))
                self.assertEqual(opener.open.call_count, 3)
                self.assertEqual(sleep.call_count, 2)

    def test_nontransient_errors_and_redirects_are_not_retried(self):
        for error in (HTTPError("url", 404, "Not Found", {}, None), HTTPError("url", 302, "Redirect", {}, None), URLError("offline")):
            with self.subTest(error=error):
                opener = Mock()
                opener.open.side_effect = error
                with patch.object(source, "build_opener", return_value=opener), patch.object(source.time, "sleep") as sleep:
                    with self.assertRaises(source.SourceError):
                        source.download(source.source_url(REF))
                self.assertEqual(opener.open.call_count, 1)
                sleep.assert_not_called()

    def test_error_cli_has_nonzero_exit_and_no_success_output(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(source, "download", side_effect=source.SourceError("Invalid reference")):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = source.main([REF])
        self.assertEqual(result, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(json.loads(stderr.getvalue()), {"error": "Invalid reference"})


if __name__ == "__main__":
    unittest.main()
