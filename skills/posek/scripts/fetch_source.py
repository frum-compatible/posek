#!/usr/bin/env python3
"""Retrieve citation evidence, never certify a halakhic interpretation.

Contract: https://developers.sefaria.org/reference/get-v3-texts
The v3 API can coerce broad references and fill gaps from other editions. This
client requires one canonical segment and disables gap filling. Live responses
expose sections/toSections/textDepth, rather than an isSegmentLevel flag; missing
or inconsistent shape information is an error. HTML and version metadata remain
unmodified, including editorial and commentator markers.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener


API_ROOT = "https://www.sefaria.org/api/v3/texts/"
MAX_BYTES = 2 * 1024 * 1024
TIMEOUT_SECONDS = 20
MAX_RETRIES = 2


class SourceError(Exception):
    """The requested source cannot be returned as citation evidence."""


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def text_state(value):
    """Inspect availability without flattening or changing the stored text."""
    if isinstance(value, str):
        parser = VisibleText()
        parser.feed(value)
        parser.close()
        return "present" if "".join(parser.parts).strip() else "missing"
    if isinstance(value, list):
        states = [text_state(item) for item in value]
        if not states or all(state == "missing" for state in states):
            return "missing"
        return "present" if all(state == "present" for state in states) else "partial"
    raise SourceError("Unexpected text shape; expected text or a nested array of text.")


def source_url(reference):
    query = urlencode([
        ("version", "source"),
        ("version", "english"),
        ("fill_in_missing_segments", "0"),
        ("return_format", "default"),
    ])
    return API_ROOT + quote(reference, safe="") + "?" + query


def download(url):
    request = Request(url, headers={
        "Accept": "application/json",
        "Accept-Encoding": "identity",
        "User-Agent": "Posek-source-evidence/0.1",
    })
    opener = build_opener(NoRedirect)
    for attempt in range(MAX_RETRIES + 1):
        try:
            with opener.open(request, timeout=TIMEOUT_SECONDS) as response:
                payload = response.read(MAX_BYTES + 1)
            if len(payload) > MAX_BYTES:
                raise SourceError("Response exceeded 2 MiB; use one exact segment reference.")
            return payload
        except HTTPError as error:
            retryable = error.code == 429 or 500 <= error.code <= 599
            error.close()
            if retryable and attempt < MAX_RETRIES:
                time.sleep(min(2 ** attempt, 2))
                continue
            raise SourceError(
                f"Sefaria returned HTTP {error.code}; no source evidence was produced. "
                "Check the exact reference, or retry later if the service is unavailable."
            ) from error
        except (URLError, TimeoutError, OSError) as error:
            raise SourceError(
                "Sefaria could not be reached within the request limits; "
                "no source evidence was produced."
            ) from error
    raise SourceError("Request attempts exhausted.")


def build_evidence(reference, raw_payload, url):
    try:
        payload = json.loads(raw_payload)
    except (ValueError, UnicodeError) as error:
        raise SourceError("Sefaria returned invalid JSON; no source evidence was produced.") from error
    if not isinstance(payload, dict):
        raise SourceError("Unexpected API response: expected an object.")
    if "error" in payload:
        raise SourceError(f"Sefaria rejected the reference: {str(payload['error'])[:300]}")

    canonical = payload.get("ref")
    if not isinstance(canonical, str) or not canonical:
        raise SourceError("Response lacks a canonical reference.")
    if canonical != reference:
        raise SourceError(
            f"Requested reference was changed to {canonical!r}. "
            "Review that reference and request its exact canonical segment explicitly."
        )
    sections = payload.get("sections")
    depth = payload.get("textDepth")
    if (
        type(depth) is not int or depth < 1
        or not isinstance(sections, list) or len(sections) != depth
        or sections != payload.get("toSections")
        or payload.get("isSpanning") is not False
    ):
        raise SourceError(
            "One exact segment is required; book, chapter, and range references are rejected. "
            "The API must supply consistent sections, toSections, textDepth, and isSpanning."
        )

    api_warnings = payload.get("warnings", [])
    if not isinstance(api_warnings, list):
        raise SourceError("Unexpected warnings field in API response.")
    warnings = list(api_warnings)
    returned_versions = payload.get("versions")
    if not isinstance(returned_versions, list) or not returned_versions:
        raise SourceError("No versions were returned; source text is unavailable.")
    versions = []
    for version in returned_versions:
        if not isinstance(version, dict) or "text" not in version:
            raise SourceError("A returned version lacks text or has an invalid shape.")
        for key in ("versionTitle", "language"):
            if not isinstance(version.get(key), str) or not version[key]:
                raise SourceError(f"A returned version lacks required {key} metadata.")
        if type(version.get("isSource")) is not bool:
            raise SourceError("A returned version lacks explicit source/translation provenance.")
        record = dict(version)
        record["text_status"] = text_state(version["text"])
        for key in ("license", "versionSource"):
            if not record.get(key):
                record.setdefault(key, None)
                warnings.append(f"{version['versionTitle']}: {key} metadata is missing.")
        if record["text_status"] != "present":
            warnings.append(
                f"{version['versionTitle']}: text is {record['text_status']}; "
                "no other edition was substituted."
            )
        versions.append(record)

    sources = [version for version in versions if version["isSource"]]
    if not sources or any(version["text_status"] != "present" for version in sources):
        raise SourceError(
            "The original-language source is missing or incomplete; "
            "a translation or alternate edition cannot replace it silently."
        )
    english = [version for version in versions if (
        version.get("actualLanguage") == "en"
        or version.get("languageFamilyName") == "english"
        or version["language"] == "en"
    )]
    if not english or any(version["text_status"] != "present" for version in english):
        warnings.append("English text is unavailable or incomplete; consult the source language.")

    return {
        "requested_ref": reference,
        "canonical_ref": canonical,
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "url": url,
        "payload_sha256": hashlib.sha256(raw_payload).hexdigest(),
        "evidence_scope": "Citation retrieval only; does not verify interpretation or a ruling.",
        "version_selection": {
            "requested": ["source", "english"],
            "fill_in_missing_segments": False,
            "return_format": "default",
            "note": "Sefaria selects its current preferred editions; inspect recorded version metadata.",
        },
        "reference_metadata": {key: payload[key] for key in (
            "sections", "toSections", "textDepth", "isSpanning"
        )},
        "versions": versions,
        "warnings": warnings,
    }


def fetch_source(reference):
    reference = reference.strip()
    if not reference or len(reference) > 500 or any(ord(char) < 32 for char in reference):
        raise SourceError("Provide one canonical segment reference of 1–500 characters.")
    url = source_url(reference)
    return build_evidence(reference, download(url), url)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", help='Exact canonical segment, e.g. "Shulchan Arukh, Orach Chayim 328:2"')
    parser.add_argument("--output", type=Path, help="Write evidence JSON here instead of standard output")
    args = parser.parse_args(argv)
    try:
        evidence = fetch_source(args.reference)
        serialized = json.dumps(evidence, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(serialized, encoding="utf-8")
        else:
            sys.stdout.write(serialized)
        return 0
    except (SourceError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
