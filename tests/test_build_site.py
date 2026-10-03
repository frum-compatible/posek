"""Offline publication checks using synthetic files only."""

import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile


SCRIPT = Path(__file__).parents[1] / "scripts" / "build_site.py"
SPEC = importlib.util.spec_from_file_location("build_site", SCRIPT)
build_site = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_site)


class GuideCodeBlocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        if tag == "code":
            self.blocks.append("")
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == "code":
            self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.blocks[-1] += data


class SiteBuildTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.scratch = Path(temporary.name)
        self.root = self.scratch / "project"
        self.output = self.scratch / "published"
        self.write("site/index.html", (
            '<link rel="canonical" href="https://frum-compatible.github.io/posek/">\n'
            '<meta property="og:image" content="https://frum-compatible.github.io/posek/social-card.png">\n'
            '<a href="https://github.com/frum-compatible/posek">Source</a>\n'
            '<a href="https://wa.me/?text=https%3A%2F%2Ffrum-compatible.github.io%2Fposek%2F">Share</a>\n'
            '<code>npx skills add frum-compatible/posek --skill posek</code>\n'
            '<a href="posek-skill.zip">Download</a>\n'
        ))
        self.write("site/social-card.png", "Synthetic image bytes")
        self.write("skills/posek/SKILL.md", "Synthetic skill instructions")
        self.write("skills/posek/LICENSE", "Synthetic license")
        self.write("skills/posek/NOTICE", "Synthetic attribution")
        self.write("skills/posek/references/source-method.md", "Synthetic source method")
        self.write("skills/posek/scripts/fetch_source.py", "# Synthetic helper\n")
        self.write("skills/posek/agents/openai.yaml", "interface: {}\n")

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def package(self, output=None):
        return build_site.package_site(
            self.root, self.output if output is None else output,
            "https://example.org/torah", "ExampleOrg/ai-torah",
        )

    def test_public_urls_and_install_command_follow_the_deployed_repository(self):
        self.package()
        html = (self.output / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="https://example.org/torah/"', html)
        self.assertIn('content="https://example.org/torah/social-card.png"', html)
        self.assertIn('href="https://github.com/ExampleOrg/ai-torah"', html)
        self.assertIn('href="https://wa.me/?text=https%3A%2F%2Fexample.org%2Ftorah%2F"', html)
        self.assertIn("npx skills add ExampleOrg/ai-torah --skill posek", html)
        self.assertIn('href="posek-skill.zip"', html)
        self.assertNotIn("frum-compatible.github.io", html)
        self.assertNotIn("frum-compatible/posek", html)

    def test_guide_contains_complete_current_markdown_with_main_skill_first(self):
        main = '---\nname: posek\n---\n\n# Full instructions\n\nאמת & truth\n'
        reference = '# Audience\n\nFirst paragraph.\n\n' + ('Complete guidance.\n' * 150)
        self.write("skills/posek/SKILL.md", main)
        self.write("skills/posek/references/audience.md", reference)
        self.write("site/skill.html", "Stale checked-in guide must not survive")
        self.package()
        html = (self.output / "skill.html").read_text(encoding="utf-8")
        parsed = GuideCodeBlocks()
        parsed.feed(html)
        self.assertEqual(parsed.blocks, [main, reference, "Synthetic source method"])
        self.assertNotIn("Stale checked-in guide", html)
        for section, path in (
            ("skill-main", "SKILL.md"),
            ("references-audience", "references/audience.md"),
            ("references-source-method", "references/source-method.md"),
        ):
            with self.subTest(section=section):
                self.assertIn(f'<section id="{section}"', html)
                self.assertIn(f'href="#{section}">{path}</a>', html)
                self.assertIn(f'href="https://github.com/ExampleOrg/ai-torah/blob/main/skills/posek/{path}"', html)

    def test_guide_escapes_embedded_html_without_changing_instruction_text(self):
        instructions = (
            '# Literal markup\n\n</code></pre><script>alert("example")</script>\n'
            '<img src="missing" onerror="example()">\n'
            'Keep &lt;this&gt;, <that>, apostrophes, "quotes", and עברית.\n'
        )
        self.write("skills/posek/SKILL.md", instructions)
        self.write("skills/posek/references/source-method.md", instructions)
        self.package()
        html = (self.output / "skill.html").read_text(encoding="utf-8")
        parsed = GuideCodeBlocks()
        parsed.feed(html)
        self.assertEqual(parsed.blocks, [instructions, instructions])
        self.assertNotIn("<script", html)
        self.assertNotIn("<img", html)

    def test_guide_metadata_resources_and_navigation_follow_deployment(self):
        self.package()
        html = (self.output / "skill.html").read_text(encoding="utf-8")
        self.assertIn('<link rel="canonical" href="https://example.org/torah/skill.html">', html)
        self.assertIn('<meta property="og:url" content="https://example.org/torah/skill.html">', html)
        self.assertIn('<meta property="og:image" content="https://example.org/torah/social-card.png">', html)
        for path in ("scripts/fetch_source.py", "LICENSE", "NOTICE"):
            with self.subTest(resource=path):
                self.assertIn(f'href="https://github.com/ExampleOrg/ai-torah/blob/main/skills/posek/{path}"', html)
        self.assertIn('href="./">Back to Posek</a>', html)
        self.assertIn('href="posek-skill.zip"', html)
        self.assertIn('rel="stylesheet" href="styles.css"', html)
        self.assertIn('class="skill-guide wrap"', html)
        self.assertNotIn("frum-compatible.github.io", html)
        self.assertNotIn("frum-compatible/posek", html)
        self.assertNotIn("<script", html)

    def test_guide_includes_only_public_direct_markdown_references(self):
        excluded = (
            "references/.private.md", "references/.hidden/notes.md",
            "references/private/notes.md", "references/work/transcript.md",
            "references/source-cache/source.md", "references/__pycache__/notes.md",
            "references/nested/appendix.md", "references/data.txt", "other.md",
        )
        for relative in excluded:
            self.write("skills/posek/" + relative, f"Do not render {relative}")
        self.package()
        html = (self.output / "skill.html").read_text(encoding="utf-8")
        parsed = GuideCodeBlocks()
        parsed.feed(html)
        self.assertEqual(parsed.blocks, ["Synthetic skill instructions", "Synthetic source method"])
        for relative in excluded:
            with self.subTest(relative=relative):
                self.assertNotIn(relative, html)
        with ZipFile(self.output / "posek-skill.zip") as archive:
            self.assertNotIn("posek/references/.private.md", archive.namelist())
            self.assertNotIn("posek/references/private/notes.md", archive.namelist())
            self.assertIn("posek/references/nested/appendix.md", archive.namelist())

    def test_skill_download_keeps_resources_and_attribution_together(self):
        self.write("private/account-notes.txt", "Private project notes")
        self.package()
        expected = {
            "posek/SKILL.md", "posek/LICENSE", "posek/NOTICE",
            "posek/references/source-method.md", "posek/scripts/fetch_source.py",
            "posek/agents/openai.yaml",
        }
        with ZipFile(self.output / "posek-skill.zip") as archive:
            self.assertEqual(set(archive.namelist()), expected)
            for name in expected:
                source = self.root / "skills" / name
                self.assertEqual(archive.read(name), source.read_bytes())
        self.assertTrue((self.output / ".nojekyll").is_file())
        self.assertEqual(
            {path.name for path in self.output.iterdir()},
            {"index.html", "skill.html", "social-card.png", "posek-skill.zip", ".nojekyll"},
        )

    def test_private_hidden_and_cache_files_are_omitted_from_both_downloads(self):
        excluded = (
            ".env", ".credentials/token.txt", "private/notes.txt",
            "work/transcript.txt", "source-cache/source.json",
            "__pycache__/helper.pyc", "helper.pyc", "helper.pyo",
        )
        for source in ("site", "skills/posek"):
            for relative in excluded:
                self.write(f"{source}/{relative}", "Must remain private")
        self.package()
        with ZipFile(self.output / "posek-skill.zip") as archive:
            for relative in excluded:
                with self.subTest(relative=relative):
                    self.assertFalse((self.output / relative).exists())
                    self.assertNotIn("posek/" + relative, archive.namelist())

    def test_output_cannot_replace_existing_files_or_live_inside_source(self):
        self.output.mkdir()
        marker = self.output / "keep.txt"
        marker.write_text("Existing work", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.package()
        self.assertEqual(marker.read_text(encoding="utf-8"), "Existing work")
        for relative in ("site/generated", "skills/posek/generated"):
            with self.subTest(relative=relative):
                output = self.root / relative
                with self.assertRaises(ValueError):
                    self.package(output)
                self.assertFalse(output.exists())

    def test_linked_files_directories_and_source_roots_are_rejected(self):
        outside = self.scratch / "external" / "outside.txt"
        outside.parent.mkdir()
        outside.write_text("Private external file", encoding="utf-8")
        for relative, target in (
            ("site/linked.txt", outside),
            ("skills/posek/references/linked.md", outside),
            ("skills/posek/references/linked", outside.parent),
        ):
            with self.subTest(relative=relative):
                link = self.root / relative
                link.symlink_to(target, target_is_directory=target.is_dir())
                try:
                    with self.assertRaises(ValueError):
                        self.package()
                    self.assertFalse(self.output.exists())
                finally:
                    link.unlink()
        for relative in ("site", "skills/posek", "skills"):
            with self.subTest(source_root=relative):
                original = self.root / relative
                moved = self.scratch / "linked-source"
                original.rename(moved)
                original.symlink_to(moved, target_is_directory=True)
                try:
                    with self.assertRaises(ValueError):
                        self.package()
                    self.assertFalse(self.output.exists())
                finally:
                    original.unlink()
                    moved.rename(original)


if __name__ == "__main__":
    unittest.main()
