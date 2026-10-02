#!/usr/bin/env python3
"""Prepare the public Pages files and a complete, portable skill download."""

import argparse
from pathlib import Path
import re
import shutil
from urllib.parse import quote, urlsplit
from zipfile import ZipFile, ZIP_DEFLATED


ROOT = Path(__file__).resolve().parents[1]
PLANNED_SITE = "https://frum-compatible.github.io/posek/"
PLANNED_REPO = "https://github.com/frum-compatible/posek"
TEXT_TYPES = {".html", ".css", ".js", ".json", ".svg", ".txt", ".xml"}
PRIVATE_DIRS = {"private", "work", "source-cache", "__pycache__"}


def publishable(path):
    return (not any(part.startswith(".") or part.lower() in PRIVATE_DIRS for part in path.parts)
            and path.suffix.lower() not in {".pyc", ".pyo"})


def public_url(value):
    parsed = urlsplit(value)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username
            or parsed.password or parsed.query or parsed.fragment
            or re.search(r'''[\s<>"'`\\]''', value)):
        raise ValueError("Use a plain HTTPS site URL without credentials, query, or fragment.")
    return value.rstrip("/") + "/"


def package_site(root, output, site_url, repository):
    site_url = public_url(site_url)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Repository must be OWNER/REPOSITORY.")
    root, output = Path(root).resolve(), Path(output).resolve()
    if output.exists():
        raise ValueError("Output directory already exists; choose a new staging directory.")
    if output == root or root in output.parents and output.parts[len(root.parts)] in {
            "site", "skills", "scripts", "tests", "benchmarks", ".git", "docs"}:
        raise ValueError("Output must be a separate staging directory.")
    site, skill = root / "site", root / "skills/posek"
    for folder in (site, root / "skills", skill):
        if folder.is_symlink() or not folder.resolve().is_relative_to(root):
            raise ValueError("Publication source folders must stay inside the repository without symlinks.")
    for required in (site / "index.html", site / "social-card.png", skill / "SKILL.md"):
        if not required.is_file():
            raise ValueError(f"Required publication file is missing: {required.name}")
    site_files = [p for p in sorted(site.rglob("*")) if p.is_file() or p.is_symlink()]
    skill_files = [p for p in sorted(skill.rglob("*")) if p.is_file() or p.is_symlink()]
    if any(p.is_symlink() for p in site_files + skill_files):
        raise ValueError("Publish regular files, not symlinks to other directories.")
    output.mkdir(parents=True)
    repository_url = "https://github.com/" + repository
    for source in site_files:
        relative = source.relative_to(site)
        if not publishable(relative):
            continue
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix in TEXT_TYPES:
            text = source.read_text(encoding="utf-8")
            text = text.replace(PLANNED_SITE, site_url).replace(PLANNED_REPO, repository_url)
            text = text.replace(quote(PLANNED_SITE, safe=""), quote(site_url, safe=""))
            text = text.replace("frum-compatible/posek", repository)
            target.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(source, target)
    with ZipFile(output / "posek-skill.zip", "w", ZIP_DEFLATED) as archive:
        for source in skill_files:
            relative = source.relative_to(skill)
            if not publishable(relative):
                continue
            archive.write(source, "posek/" + relative.as_posix())
    (output / ".nojekyll").write_text("", encoding="utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--site-url", default=PLANNED_SITE)
    parser.add_argument("--repository", default="frum-compatible/posek")
    args = parser.parse_args()
    try:
        destination = package_site(ROOT, args.output, args.site_url, args.repository)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Site packaging failed: {error}\n")
    print(f"Prepared public files in {destination}; no deployment was performed.")


if __name__ == "__main__":
    main()
