"""Exercise the published phone page in Chromium on GitHub CI only."""

from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
import sys
from threading import Thread
from urllib.parse import unquote, urlsplit


APPS = {
    "ChatGPT": "https://chatgpt.com/#native",
    "Claude": "https://claude.ai/new",
    "Gemini": "https://gemini.google.com/app",
    "Muse": "https://muse.ai/",
}


@contextmanager
def serve_site(directory):
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}/"
        finally:
            server.shutdown()
            thread.join(timeout=5)


def check_page(page, url, artifacts, expect):
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(url)
    public_url = page.locator('link[rel="canonical"]').get_attribute("href")
    parsed = urlsplit(public_url)
    assert parsed.scheme == "https" and parsed.netloc and public_url.endswith("/")
    assert not parsed.query and not parsed.fragment
    repository_url = page.locator('#install a[href^="https://github.com/"]').get_attribute("href")
    skill_url = repository_url.rstrip("/") + "/blob/main/skills/posek/SKILL.md"
    prompt = page.locator("#prompt")
    default = prompt.input_value()
    assert default.startswith(f"Read and apply the Posek skill:\n{skill_url}")
    assert public_url + "skill.html" in default
    assert all(text in default for text in ("source-method", "hashkafah", "ask me to paste the skill"))
    assert "inline instructions" not in default
    assert not page.locator(".prompt-details").evaluate("element => element.open")
    assert page.locator("[data-open-app]").count() == len(APPS)
    for width in (320, 390):
        page.set_viewport_size({"width": width, "height": 844})
        page.screenshot(path=str(artifacts / f"default-{width}.png"), full_page=True)
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at {width}px"

    question = 'Explain this minhag, keeping <these words> & "this quotation".'
    page.locator("#question").fill(question)
    page.locator("#profile-trigger").click()
    page.locator('label:has(input[name="profile-choice"][value="modern-orthodox"])').click()
    page.locator("details.advanced > summary").click()
    page.locator("#register").select_option("hebrew")
    page.locator("#depth").select_option("iyun")
    custom = prompt.input_value()
    assert all(text in custom for text in (question, "Modern Orthodox", "Register: Hebrew", "Depth: Iyun"))
    page.locator("#copy-prompt").click()
    expect(page.locator("#copy-status")).to_have_text("Copied.")
    assert page.evaluate("navigator.clipboard.readText()") == custom
    assert page.url == url
    page.locator("#copy-link").click()
    expect(page.locator("#share-status")).to_have_text("Public link copied.")
    assert page.evaluate("navigator.clipboard.readText()") == public_url
    for href in page.locator(".whatsapp-share").evaluate_all("links => links.map(link => link.href)"):
        assert public_url in unquote(href) and question not in unquote(href)

    page.locator('label:has(input[name="mode"][value="torah"])').click()
    page.locator("#question").fill("Prepare a vort about Avraham.")
    page.locator("#audience").select_option("ladies")
    page.locator("#sources").select_option("tanach")
    torah = prompt.input_value()
    assert all(text in torah for text in ("Prepare a vort about Avraham.", "Ladies' Parsha Shiur", "Tanach and mefarshim", "omit Gemara analysis"))
    assert "divrei-torah, torah-writing, and audience" in torah

    for name, destination in APPS.items():
        page.goto(url)
        page.locator("#question").fill(f"A distinct question for {name}.")
        copied = prompt.input_value()
        button = page.locator(f'[data-app-name="{name}"]')
        assert button.get_attribute("data-open-app") == destination
        button.click()
        page.wait_for_url(destination)
        assert page.evaluate("navigator.clipboard.readText()") == copied
        page.goto(url)
        page.evaluate("navigator.clipboard.writeText = async () => { throw new Error('Denied for test'); }")
        button.click()
        expect(page.locator("#manual-copy")).to_be_visible()
        assert page.url == url
        assert page.locator("#manual-text").input_value() == prompt.input_value()
    assert not errors, errors


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("Run this browser smoke test on GitHub Actions, not the local machine.")
    from playwright.sync_api import expect, sync_playwright

    site = Path(sys.argv[1]).resolve()
    artifacts = Path(sys.argv[2]).resolve()
    assert (site / "index.html").is_file(), "Build the public site first."
    artifacts.mkdir(parents=True, exist_ok=True)
    with serve_site(site) as url, sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            context = browser.new_context(permissions=["clipboard-read", "clipboard-write"], service_workers="block")
            try:
                # External navigation is fulfilled locally: provider sites are never contacted.
                context.route("**/*", lambda route: route.continue_() if route.request.url.startswith(url)
                              else route.fulfill(content_type="text/html", body="<title>Handoff captured</title>"))
                check_page(context.new_page(), url, artifacts, expect)
            finally:
                context.close()
        finally:
            browser.close()
    print("Phone prompt, clipboard handoffs, share privacy, and mobile layout passed.")


if __name__ == "__main__":
    main()
