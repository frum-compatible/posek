#!/usr/bin/env python3
"""CI-only integrity checks; these do not evaluate halakhic correctness."""

from collections import Counter
import importlib.util
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("posek_score", ROOT / "benchmarks/score.py")
score = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    skill = ROOT / "skills/posek"
    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
    require(match is not None, "SKILL.md needs YAML frontmatter")
    fields = dict(line.split(":", 1) for line in match[1].splitlines() if ":" in line)
    require(fields.get("name", "").strip() == skill.name, "Skill name must match its folder")
    require(bool(fields.get("description", "").strip()), "Skill description is required")
    require((skill / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(),
            "Installed skill must retain its MIT license")

    cases = score.validate_cases(score.read_json(ROOT / "benchmarks/cases.json"))
    manifest = json.loads((ROOT / "benchmarks/source-manifest.json").read_text())
    # Source-manifest field names are deliberately explicit; its data is provenance,
    # not proof of either benchmark labels or source-text authenticity.
    require(isinstance(manifest, dict), "Source manifest must be an object")
    require(isinstance(manifest.get("sources"), list), "Manifest sources must be a list")
    source_refs = {item["ref"] for item in manifest["sources"]}
    pairs = Counter()
    for case in cases:
        for key in ("expected_behavior", "critical_failures"):
            require(isinstance(case.get(key), list) and case[key]
                    and all(isinstance(item, str) and item.strip() for item in case[key]),
                    f"{case['id']}: {key} must contain nonempty strings")
        require(isinstance(case.get("source_refs"), list), f"{case['id']}: source_refs required")
        require(set(case["source_refs"]) <= source_refs,
                f"{case['id']}: source reference missing from provenance manifest")
        pair = case.get("pair_id")
        require(pair is None or isinstance(pair, str) and bool(pair.strip()),
                f"{case['id']}: invalid pair_id")
        if pair:
            pairs[pair] += 1
    require(all(count >= 2 for count in pairs.values()), "A counterfactual group needs at least two cases")

    editorial_cases = score.validate_cases(score.read_json(ROOT / "benchmarks/divrei-torah/cases.json"))
    semicha_cases = score.validate_cases(score.read_json(ROOT / "benchmarks/semicha/questions.json"))
    for case in editorial_cases:
        require(case.get("mode") in ("generation", "revision"), f"{case['id']}: invalid editorial mode")
        for key in ("review_checks", "critical_failures"):
            require(isinstance(case.get(key), list) and case[key]
                    and all(isinstance(item, str) and item.strip() for item in case[key]),
                    f"{case['id']}: {key} must contain nonempty strings")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            require((path.parent / target).exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}")

    for runs_dir, run_cases in ((ROOT / "benchmarks/runs", cases),
                                (ROOT / "benchmarks/semicha/runs", semicha_cases)):
        for judgments_path in sorted(runs_dir.glob("*/judgments.json")):
            expected = score.score_judgments(score.read_json(judgments_path), run_cases, judgments_path.parent)
            saved = score.read_json(judgments_path.with_name("report.json"))
            require(saved == expected, f"Stale or altered report: {judgments_path.parent.name}")

    development = ROOT / "benchmarks/semicha/development"
    repair_review = score.read_json(development / "review.json")
    require(len(repair_review["judgments"]) == 1, "Development rerun needs one recorded judgment")
    require(repair_review["judgments"][0]["response_sha256"]
            == score.response_digest("response.md", development), "Development response changed after review")
    published_rulings = ROOT / "benchmarks/published-rulings"
    for case in score.read_json(published_rulings / "cases.json")["cases"]:
        review = score.read_json(published_rulings / "review" / f"{case['id']}.json")
        require(review["response_sha256"]
                == score.response_digest(f"responses/{case['id']}.md", published_rulings),
                f"Published-ruling response changed after review: {case['id']}")
    print(f"Project structure and saved reports checked; {len(cases)} psak, {len(editorial_cases)} editorial, and {len(semicha_cases)} semicha-derived cases. No accuracy claim.")


if __name__ == "__main__":
    main()
