# Phone and WhatsApp distribution

The landing page in `site/` explains Posek, shows a dvar Torah, and prepares a phone starter prompt. A recipient can read it without installing a terminal skill or creating an account on this site. Halacha opens by default; “No question? Try a shailah” offers five [source-based examples](../examples/SHAILOS.md) that fill the editable question box.

## Open an AI app

The ChatGPT, Claude, Gemini, and Muse buttons copy the generated prompt, then navigate to the chosen service in the same tab. The visitor pastes into a new chat and sends it. The destination URL contains no question text. If clipboard access fails, the page stays open with selectable text and destination links. Copy prompt only copies without opening anything, then offers ordinary app and browser links.

The copied message starts with the [GitHub skill](https://github.com/frum-compatible/posek/blob/main/skills/posek/SKILL.md) and [complete reference guide](https://frum-compatible.github.io/posek/skill.html), then gives the selected settings and question. It tells the AI to browse the main skill and relevant references before answering. The guide includes SKILL.md and every direct Markdown reference guide, rebuilt during publication. The default prompt carries no duplicate inline skill; web access is expected. If neither link can be read, it asks the AI to report that and request the skill text. No installation is required. The prompt preview is collapsed by default.

The ChatGPT destination is `https://chatgpt.com/#native`. OpenAI's [iOS association file](https://chatgpt.com/.well-known/apple-app-site-association) explicitly maps this path and fragment to a new conversation in the app. Its [Android association file](https://chatgpt.com/.well-known/assetlinks.json) verifies the `com.openai.chatgpt` app for this domain. These are app-eligible HTTPS links with a web destination when no app handles them; app versions, browser behavior, and device preferences still matter. The browser option uses `?no_universal_links=1`, which the iOS association file explicitly excludes from native routing. Android behavior also depends on the installed app's link handling.

Copy prompt only exposes a directly tappable Open ChatGPT app link after a successful copy. That gives the phone a fresh user action if the combined copy-and-open route stayed in the browser. The browser fallback and links to the other services are beside it. Editing the question or settings hides these links until the updated prompt is copied. [Apple's universal-link guidance](https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links/) and [Android App Links](https://developer.android.com/training/app-links/about) describe the platform behavior. The page does not detect app installation or submit a prompt automatically.

Official documentation checked on 2 October 2026 covers [ChatGPT desktop deep links](https://learn.chatgpt.com/docs/reference/commands), [Claude desktop links](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link), and [Claude mobile Code links](https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link). Those documented routes do not establish a general-chat prefill method across mobile browsers and both services, so the phone flow uses clipboard handoff.

Gemini opens `https://gemini.google.com/app`, the web app described in [Google's instructions](https://support.google.com/gemini/answer/13275745?hl=en). Muse opens `https://muse.ai/`, linked in [Meta's launch announcement](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/). These buttons use the same clipboard handoff; Posek does not require an API integration or pass the question in a URL. Native-app opening for these services has not been verified.

The receiving AI reads the linked instructions and checks sources with its own tools. Opening a service alone does not paste or submit the prompt. The page itself does not answer shailos or send questions to an AI service.

## What sharing does

The WhatsApp button opens a prefilled message containing public introductory copy and the public page URL. The person chooses the recipient and sends it. It never includes the question typed into the page. Native sharing and Copy link use the same public URL. The page uses no analytics, account system, or server submission.

The share caption is:

> Posek AI — An Orthodox AI Rabbi. Hashkafah: configurable. Mareh mekomos: required. Mutar is also a psak.

The public link follows that caption. See [WhatsApp's click-to-chat documentation](https://faq.whatsapp.com/5913398998672934).

## Publish the page

The public page is [frum-compatible.github.io/posek](https://frum-compatible.github.io/posek/). Its first deployment completed on 2026-10-02.

After authenticating as the intended personal GitHub account and publishing the reviewed repository:

1. In the repository's Settings, open Pages and select GitHub Actions as the publishing source.
2. Run the **Publish phone site** workflow from Actions. It runs the project checks, prepares the public files, and deploys them.
3. Open the URL reported by the deployment and check it on an actual phone.
4. Send the link to yourself in WhatsApp and inspect the preview before sharing more widely.

The workflow uses GitHub's reported site URL and repository name to replace the planned links. `scripts/build_site.py` packages the static page and a complete `posek-skill.zip`. It copies no personal skill inventory, working evidence, or account configuration.

The public page URL stays the same across releases. Published script and stylesheet URLs include hashes of their final contents, so a fresh page fetch uses the matching assets. An already-open tab still needs a reload. During diagnosis on 2 October, GitHub Pages served a ten-minute cache lifetime; cached HTML may take time to refresh too.

The workflow is manual. A push alone does not publish or update the site. See [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Link preview

The HTML includes a title, description, canonical URL, and absolute Open Graph image URL. The preview image is a 1200 × 630 PNG rendered from `site/social-card.html`. These fields follow the [Open Graph specification](https://ogp.me/).

A crawler must be able to retrieve the published HTTPS page and image. Local previews cannot establish that WhatsApp will show the final card. WhatsApp may cache an earlier preview; inspect the actual published link before announcing it.

## Local preparation

Render `site/social-card.html` at 1200 × 630 and save the image as `site/social-card.png`. Then prepare a fresh output directory:

```sh
python3 scripts/build_site.py --output work/site-preview
```

The output directory must not already exist. Use a temporary local server for browser inspection and stop it afterward. Keep gates on GitHub CI. The local browser check covers the page and controls, not external WhatsApp delivery or model accuracy.
