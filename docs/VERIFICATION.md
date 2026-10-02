# Verification record

Recorded on 2026-10-02. Publication and GitHub CI are pending.

## Skill behavior and sources

The source helper retrieved exact live segments with original text and edition metadata. The [psak pilot](../benchmarks/RESULTS.md) preserves nine selected cases for Posek and a no-skill baseline. Both passed all nine under AI review; this does not demonstrate an improvement from the skill.

Four later, independent candidate sessions exercised the divrei Torah workflow. Their [saved outputs and review](../benchmarks/divrei-torah/RESULTS.md) include source findings and editorial weaknesses. These runs predate the final profile and audience additions. No qualified human validation or general halachic accuracy rate is claimed.

## Local installation

Codex discovered Posek as an enabled skill without a parser error or duplicate entry. Claude Code's skill link resolves to the same complete bundle. The installed 12-file bundle matches the project source, including the reference guides, source helper, license, and notice. An end-to-end Claude invocation was not tested.

## Phone page

Manual browser inspection covered the built page at 320, 390, and 1440 pixels wide. The narrowest viewport had no horizontal page overflow. Desktop and mobile screenshots were inspected. No browser console errors or warnings were observed during the page check.

The following interactions were exercised:

- Ladies' Parsha Shiur uses the traditional source plan under Modern Yeshivish and permits Gemara under Open Orthodox. Women's Beis Medrash permits Gemara under Lakewood Yeshivish.
- An explicit source preference takes precedence for a dvar Torah. Practical psak disables that presentation preference and requests all controlling sources.
- A typed question appears in the generated prompt and stays out of the public share URL.
- Copying the starter reports success. When clipboard access is unavailable, a manual-copy field contains the same text.
- The built page, social image, and complete skill ZIP were served successfully. The 1200 × 630 social card was rendered and inspected.

These checks verify page behavior, not the quality of an AI answer generated from every setting. The page was inspected through browser viewport emulation; an actual phone and the live WhatsApp preview remain to be checked after publication. No WhatsApp message was sent. Temporary preview servers were stopped.

## Software gates

The repository contains 34 offline unit tests covering source retrieval, evaluation scoring, and site packaging, plus a project consistency check. They have not been run locally, in accordance with the author's CI-only machine policy. Both GitHub workflows run the checks before their respective jobs complete; the Pages workflow deploys only after they pass.

The repository has no public remote or commit at the time of this record. Local inspection and artifact generation do not establish a passing CI run. Use the [publishing guide](PUBLISHING.md) to authenticate with the intended account, commit, push, and inspect the actual results.
