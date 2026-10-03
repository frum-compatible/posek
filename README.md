# Posek AI — An Orthodox AI Rabbi for Torah and Halacha

**Moirah D’Asrah**

An open-source AI Posek for shailos in halacha and divrei Torah, built for halachic rigor in Claude Code and Codex. Learn the sugya and give a clear answer with mareh mekomos.

Mutar is also a psak. A heter requires a source. So does an issur.

## Start on your phone

The [phone page](https://frum-compatible.github.io/posek/) opens on Halacha. Choose your hashkafah, write your question, and use Copy & open ChatGPT, Claude, Gemini, or Muse; paste the prompt in the new chat. No question in mind? Try one of five [sample shailos](examples/SHAILOS.md) about a rental kitchen, tasting cholent, childbirth on Shabbos, babysitting, and an airline roll. Switch to Dvar Torah for a vort, shiur, or draft revision. Language, depth, and teaching preferences are under Advanced settings. The complete installed skill includes the longer source method and reference guides.

The short prompt starts with the [GitHub skill](https://github.com/frum-compatible/posek/blob/main/skills/posek/SKILL.md) and [full reference guide](https://frum-compatible.github.io/posek/skill.html), followed by your settings and question. It tells the AI to read the skill online before answering. Use a chat with web access. The prompt preview stays closed until you open it. Copy prompt only stays on the page. ChatGPT's opening link supports native-app routing, with a browser option available; you still paste and send in the new chat.

WhatsApp sharing sends the public introduction and page link. It leaves your question out. GitHub Pages hosts the public site. The [phone and WhatsApp guide](docs/PHONE-SHARING.md) covers deployment and the live preview check.

The page includes recommended ChatGPT and Claude setups. Read the [model and source-access guide](docs/MODEL-SETUP.md) for current suggestions and their limits. For a practical shailah, confirmation with your local rav is recommended. Bring the mareh mekomos.

## AI Torah learning and practical shailos

Posek approaches a shailah by clarifying the metzius before applying the din. Each teshuvah should explain how the sources bear on the case. Where the sources and circumstances support a psak, the answer should be clear: mutar, assur, or mutar under stated conditions.

The method distinguishes the Mechaber from the Rema, ikar hadin from a chumrah, and a communal minhag from a personal practice. A machlokes remains a machlokes. A heter needs a basis in the poskim, and so does an issur.

For each source, Posek checks the original lashon against the translation and gives the relevant siman and se’if. If a missing fact or an unresolved source prevents a conclusion, it identifies what must be clarified.

## Choose a hashkafah

Hashkafah: configurable. Mareh mekomos: required.

Select a profile in ordinary language. Posek uses it to decide how to explain the shailah and which sources to investigate. State your minhag and requested posek separately when they matter.

| Profile | Setting |
| --- | --- |
| Lakewood Yeshivish | Yeshivah and Kollel |
| Modern Yeshivish | The Working Ben Torah |
| Out-of-Town Yeshivish | The Community Beis Medrash |
| Modern Orthodox | Torah U'Madda |
| Open Orthodox | Halachah and Kehillah |
| Torah im Derech Eretz | Kehillah and Mesorah |
| Dati Leumi | Toras Eretz Yisrael |
| Chassidish | Derech HaChassidus |

The Lakewood setting uses a familiar beis-medrash register. Modern Orthodox defaults to a more accessible explanation, with technical terms explained where needed. You can ask either profile for more iyun or a shorter answer. The [profile guide](skills/posek/references/hashkafah.md) describes each setting and how to request a custom combination.

For practical psak, a change in the conclusion needs a difference in the facts or applicable sources. A profile name does not establish a family's minhag or a rav's position. Posek can compare documented practices without inventing one ruling for everyone in a community.

Choose the audience and depth separately. Ladies' Parsha Shiur uses an editable source plan for the selected hashkafah; Women's Beis Medrash can use Gemara under any profile. Explicit source requests take precedence. The [audience guide](skills/posek/references/audience.md) explains these defaults and the accessible, developed, and iyun settings.

```text
Use Posek. Hashkafah: Modern Yeshivish, The Working Ben Torah.
Follow the family minhag I describe. Give the psak first,
then enough of the sugya to explain it.
```

## Divrei Torah, vortlach, and shiur preparation

Divrei Torah have their own seder. Posek starts with the pesukim, sugya, or mefarshim and develops one point for the requested audience and occasion. A Shabbos-table vort needs a different treatment from a derashah, a shiur outline, or a source sheet.

For yeshivish English, short source quotations appear in Hebrew within the English explanation. The included Anti-Slop writing guide cuts generic openings and repeated explanations, with sentences written for spoken delivery. Read [פכים קטנים](examples/pachim-ketanim.md) for a finished example.

- A kushya must survive a reading of the passage in context. Posek checks the difficulty before building a teretz on it.
- Each mareh makom must establish something the argument needs. Posek distinguishes pshat, derash, the mefaresh’s position, and a proposed chiddush.
- The conclusion must follow from the source. A textual insight can stand on its own; Posek checks for endings that could be attached to almost any parsha.
- Bring an existing draft for revision. Posek checks its attributions and reasoning, preserves the sound idea, and cuts repetition. A quotation attributed to a gadol must be verified before it is used.

The installable skill includes guidance on spoken length, audience, source sheets, current-parsha lookup, and attribution of original suggestions. Read the [development examples and review](benchmarks/divrei-torah/RESULTS.md) for actual outputs produced during forward testing.

## Install

Install from the public repository:

```sh
npx skills add frum-compatible/posek --skill posek --agent claude-code --agent codex
```

For a local checkout, copy `skills/posek` into your target project's `.agents/skills/` for Codex or `.claude/skills/` for Claude Code. Preserve the entire folder, including references and scripts. Reload your host if necessary. See the current [Codex skill documentation](https://developers.openai.com/codex/skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

Invoke `$posek` in Codex or `/posek` in Claude Code, followed by your question. The skill can also be selected automatically for matching questions.

For source verification, the host needs browsing or Python 3.10+ with outbound HTTPS. The bundled Sefaria helper uses only the standard library and needs no API key. With no retrieval tools, the skill works from supplied passages and identifies what it cannot verify. Local Codex discovery and Claude Code's skill links were verified; an end-to-end Claude invocation remains untested. See the [verification record](docs/VERIFICATION.md).

## Ask a useful question

```text
Use Posek. I already said ha'adamah over an ordinary apple.
Did that fulfill the initial blessing? Would ha'etz over an ordinary
cucumber work the same way? Show the source and distinguish the two cases.
```

```text
Compare the Mechaber and Rema on the tefillin blessings when there is
no interruption. My family practice is unknown. Don't silently choose it.
```

```text
Someone claims a shul with eleven windows is invalid because twelve
are required. Does Orach Chayim 90:4 actually establish that?
```

```text
Use Posek to prepare a three-minute dvar Torah about Yaakov’s
pachim ketanim. Develop one real point from the Gemara and its context.
Keep it under 450 spoken words; put mareh mekomos afterward.
```

```text
Here is my draft vort. Check the sources and attributions, preserve
the idea if it works, and improve the argument before polishing the language.
The audience is teenagers; I have two minutes.
```

A straightforward shailah should receive a straightforward answer. A more involved shailah calls for the relevant tzedadim, mareh mekomos, and a clear explanation of what can be concluded l’maaseh.

## Inspect a source

From the repository root:

```sh
python3 skills/posek/scripts/fetch_source.py \
  'Shulchan Arukh, Orach Chayim 202:1'
```

The helper records the canonical reference, original text, English when available, edition metadata, warnings, retrieval time, and a response hash. It refuses silent reference changes and missing original text. The returned text still needs to be read and interpreted.

During development, an inspected English translation of O.C. 202:1 rendered the Hebrew for cooked wine as diluted wine. Check the original lashon wherever wording affects the din. The [evidence ledger](benchmarks/SOURCES.md) records the inspected versions and other source issues.

## Evaluation

The practical halacha suite contains 24 development cases: bounded source reading, factual counterfactuals, minhag, mistaken citations, retrieval failure, and consequential-case boundaries. A [separate ten-case divrei Torah suite](benchmarks/divrei-torah/README.md) covers generation, revision, weak arguments, attribution, length, and attempts to turn a vort into a heter. These are AI-drafted development criteria requiring qualified human review.

See [the protocol](benchmarks/README.md) and [recorded results](benchmarks/RESULTS.md). These are development observations, not a percentage of “halakhic accuracy,” rabbinic certification, or evidence of superiority to human poskim. Public development cases also cannot establish performance on unseen questions.

The [semicha-question pilot](benchmarks/semicha/RESULTS.md) adds four adapted public items from the Chief Rabbinate and a WebYeshiva semicha course. Eight fresh sessions produced 46/48 rubric points for Posek and 48/48 for the no-skill assistant under independent AI source review. The report documents the omission that prompted a skill revision. These are selected questions, not a full examination or a comparison with rabbonim.

[Read the four questions and both sets of answers](benchmarks/semicha/QUESTIONS.md), with original source links and item-by-item review.

Two [published-ruling cases](benchmarks/published-rulings/RESULTS.md) check whether a heter survives together with its limits. Both answers received supported findings under AI source review. Their purpose is to catch an unnecessary issur as well as an overbroad heter.

The repository includes offline tests and GitHub Actions workflows. These check software behavior separately from the halachic and editorial evaluations; see the [verification record](docs/VERIFICATION.md) for actual CI runs. The original psak pilot predates the current wording and divrei Torah mode; its answers and skill hashes are preserved. The newer divrei Torah runs have their own input records and review.

## Scope

This is experimental religious-reasoning software. It may misread a source, miss a later authority, or apply a rule to the wrong facts. The skill gives direct answers to ordinary supported questions and calls out the cases that require qualified personal judgment. It cannot issue an actual get, conversion, court decision, kashrut certificate, or institutional endorsement. Possible emergencies come before source lookup.

“AI Rabbi” describes the software’s role; no semichah, rabbinic haskamah, or institutional endorsement is claimed. There is no affiliation with an actual shul, yeshiva, posek, Sefaria, Anthropic, or OpenAI.
Yeshivas Birur HaDavar, Lakewood, is the fictional institution used by the AI persona.

## Contribute

Bring the shailah, the relevant metzius, and the mareh mekomos. Explain where the reasoning needs correction and whether the change affects the psak l’maaseh.

See [CONTRIBUTING.md](CONTRIBUTING.md). Never submit private she'eilot or identifiable personal circumstances without permission. Source-text corrections should also go to the relevant publisher or edition maintainer when appropriate.

## Publish your own copy

[Publishing guide](docs/PUBLISHING.md): personal GitHub identity, pseudonyms, work-account separation, and discovery. [Launch copy](docs/LAUNCH.md) is ready to adapt after there is a public repository and verified result to link.

MIT for this project's original material. Retrieved source editions retain their own licenses; see [NOTICE](NOTICE).
