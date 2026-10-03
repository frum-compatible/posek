# Phone and WhatsApp distribution

The landing page in `site/` explains Posek, shows a dvar Torah, and prepares a phone starter prompt. A recipient can read it without installing a terminal skill or creating an account on this site. Halacha opens by default; “No question? Try a shailah” offers five [source-based examples](../examples/SHAILOS.md) that fill the editable question box.

## Open an AI app

Copy & open ChatGPT and Copy & open Claude copy the complete generated prompt, then navigate to the chosen service in the same tab. The visitor pastes into a new chat and sends it. The destination URL contains no question text. If clipboard access fails, the page stays open with selectable text and ordinary links to both services. Copy full prompt is also available without opening another app.

The copied message defines Posek's role and supplies the phone instructions directly. It does not ask ChatGPT or Claude to recognize a skill name or load an installed package. The page says to paste and send next to the app buttons; opening an app alone does not transfer the instructions into its chat.

The app buttons use HTTPS links. They do not promise a native-app launch or automatic prompt submission. Sign-in and the phone's link handling remain outside this page's control.

Official documentation checked on 2 October 2026 covers [ChatGPT desktop deep links](https://learn.chatgpt.com/docs/reference/commands), [Claude desktop links](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link), and [Claude mobile Code links](https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link). Those documented routes do not establish a general-chat prefill method across mobile browsers and both services, so the phone flow uses clipboard handoff.

The starter prompt is self-contained but shorter than the installed skill. Users paste it into their own AI app. Source verification depends on that app's tools. The page itself does not answer shailos or send questions to an AI service.

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
