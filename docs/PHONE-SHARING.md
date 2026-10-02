# Phone and WhatsApp distribution

The landing page in `site/` explains Posek, shows an excerpt from an actual dvar Torah, and prepares a phone starter prompt. A recipient can read it without installing a terminal skill or creating an account on this site.

The starter prompt is self-contained but shorter than the installed skill. Users paste it into their own AI app. Source verification depends on that app's tools. The page itself does not answer shailos or send questions to an AI service.

## What sharing does

The WhatsApp button opens a prefilled message containing public introductory copy and the public page URL. The person chooses the recipient and sends it. It never includes the question typed into the page. Native sharing and Copy link use the same public URL. The page uses no analytics, account system, or server submission.

The share caption is:

> Posek — An Orthodox AI Rabbi for Torah, halacha and divrei Torah. Choose your hashkafah and prepare a prompt that asks for exact mareh mekomos.

The public link follows that caption. See [WhatsApp's click-to-chat documentation](https://faq.whatsapp.com/5913398998672934).

## Publish the page

The intended initial URL is `https://frum-compatible.github.io/posek/`. It is a planned URL until the repository and Pages deployment exist.

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
