# Verification record

Recorded on 2026-10-02. The repository and phone page are public.

## Skill behavior and sources

The source helper retrieved exact live segments with original text and edition metadata. The [psak pilot](../benchmarks/RESULTS.md) preserves nine selected cases for Posek and a no-skill baseline. Both passed all nine under AI review; this does not demonstrate an improvement from the skill.

Four later, independent candidate sessions exercised the divrei Torah workflow. Their [saved outputs and review](../benchmarks/divrei-torah/RESULTS.md) include source findings and editorial weaknesses. These runs predate the final profile and audience additions. No qualified human validation or general halachic accuracy rate is claimed.

## Local installation

Codex discovered Posek as an enabled skill without a parser error or duplicate entry. Claude Code's skill link resolves to the same complete bundle. The installed 12-file bundle matches the project source, including the reference guides, source helper, license, and notice. An end-to-end Claude invocation was not tested.

## Phone page

Manual browser inspection covered the built page at 320, 390, and 1440 pixels wide. The narrowest viewport had no horizontal page overflow. Desktop and mobile screenshots were inspected. No browser console errors or warnings were observed during the page check.

The following interactions were exercised:

- The simplified entry flow starts on Halacha with Advanced settings closed. Only the hashkafah selector and question box precede the copy action. The mode switch works with both clicks and arrow keys.
- The hashkafah picker displays separate names and subtitles, keeps Modern Yeshivish as the default, and follows a rough traditional-to-modern ordering. Pointer selection, native radio arrow navigation, Enter, Escape, Tab, and outside dismissal were exercised. Deferring the focus-leave check avoids dismissing the options before a label click finishes.
- Halacha and Dvar Torah retain separate question text, register, and depth during mode switches. Hashkafah remains shared. Hidden Torah format, audience, and source choices do not enter the Halacha prompt; returning to Dvar Torah restores them.
- Ladies' Parsha Shiur uses the traditional source plan under Modern Yeshivish and permits Gemara under Open Orthodox. Women's Beis Medrash permits Gemara under Lakewood Yeshivish.
- An explicit source preference takes precedence for a dvar Torah. Practical psak disables that presentation preference and requests all controlling sources.
- A typed question appears in the generated prompt and stays out of the public share URL.
- Copying the starter reports success. When clipboard access is unavailable, a manual-copy field contains the same text.
- Each sample fills the question box and generated prompt without changing the selected hashkafah. The picker is hidden in Dvar Torah mode, and the Halacha sample returns when switching back.
- Copy & open reached the ChatGPT page and Claude's new-chat/sign-in flow in the browser. A clipboard write was read back immediately and matched the generated prompt. With clipboard access unavailable, the handoff stayed on Posek and exposed matching manual-copy text and destination links. Native-phone launching and clipboard retention through an actual phone's app switch remain unverified.
- The built page, social image, and complete skill ZIP were served successfully. The 1200 × 630 social card was rendered and inspected.

These checks verify page behavior, not the quality of an AI answer generated from every setting. The page was inspected through browser viewport emulation; an actual phone and the live WhatsApp preview remain to be checked after publication. No WhatsApp message was sent. Temporary preview servers were stopped.

Before the link-first revision, the longer inline phone prompt was also pasted and sent in a fresh, signed-out ChatGPT web session. With no installed Posek skill, it answered the completed-bentching/Rosh Chodesh example and supplied source citations. A separate fresh-context assistant check also answered from the supplied instructions without loading the skill. These are narrow prompt-usability checks, not additions to the accuracy benchmark. Neither reproduces clipboard transfer through a native iPhone app switch.

## Link-first phone update

A user supplied the full prompt copied on an iPhone. It matched the earlier inline version and contained no links. At the same time, HTTP reads of the published JavaScript matched the newer repository source and included both skill URLs. The page still referenced unversioned assets; GitHub Pages returned `Cache-Control: max-age=600`. This identifies an older page or cached script in use, without distinguishing between those two causes.

The replacement prompt starts with the GitHub skill and full-guide URLs, then supplies settings and the question. Browsing is the expected path; the inline duplicate has been removed. The preview stays collapsed. Published JS and CSS references now carry hashes of their final contents. The public URL and shared links remain unchanged. Already-open pages must still reload.

Gemini and Muse use the existing copy-and-open handler. Browser smoke checks on CI cover all four destinations, the copied text, manual-copy fallback, settings, privacy of shared links, and narrow layouts. External navigation is intercepted in these checks; they do not establish native-app routing, account availability, or answer quality in any receiving service. No local browser or server was opened for this revision. The earlier ChatGPT answer check above does not validate this new link-reading flow.

## Software gates

At revision a8f605a, all 34 offline unit tests covering source retrieval, evaluation scoring, and site packaging passed alongside the project consistency check on [GitHub CI at revision a8f605a](https://github.com/frum-compatible/posek/actions/runs/37059777121). They were not run locally, in accordance with the author's CI-only machine policy. Both GitHub workflows run the checks before their respective jobs complete; the Pages workflow deploys only after they pass.

The [Pages deployment](https://github.com/frum-compatible/posek/actions/runs/37059836316) published that revision. The public HTML, social-card image, and skill ZIP returned HTTP 200. A browser inspection of the live page at 390 pixels confirmed the public canonical URL, generated starter, correct WhatsApp URL, hidden local-preview notice, and no horizontal overflow. The live WhatsApp card inside WhatsApp remains unverified; no message was sent.

The publishing identity is `frum-compatible`, with its GitHub noreply address in author and committer metadata. Authentication uses a separate CLI configuration. An inherited HTTPS-to-SSH URL rewrite required a repository-local rule to keep this repository on HTTPS; global work configuration was preserved. Use the [publishing guide](PUBLISHING.md) for subsequent updates and inspect the CI run for the exact revision being released.
