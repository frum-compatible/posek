# Posek AI — An Orthodox AI Rabbi for Torah and Halacha

**Moirah D’Asrah**

Mutar is also a psak. A heter requires a source. So does an issur.

Hashkafah: configurable. Mareh mekomos: required. For a practical shailah, confirmation with your local rav is recommended. Bring the mareh mekomos.

Posek is an open-source AI Posek for Claude Code and Codex, built for halachic rigor. Bring a shailah with the relevant metzius. Posek opens the sources and works through the halacha to a practical conclusion with mareh mekomos.

Psak begins with the Shulchan Aruch and the later poskim needed for the particular shailah. Posek distinguishes the Mechaber from the Rema and checks the original lashon. The teshuvah should explain the basis for its conclusion, including any fact that could change the answer. Where the sources support a clear answer, it says mutar or assur and gives the conditions.

Posek distinguishes l’chatchilah from b’dieved, and din from minhag or a personal chumrah. Where there is a machlokes, it explains the relevant shitos and how an established minhag affects the psak. If a material fact is missing, Posek asks before drawing a conclusion.

Choose a hashkafah profile, including Lakewood Yeshivish, Modern Yeshivish, Modern Orthodox, or Open Orthodox. Posek adjusts the language and chooses sources to investigate for the requested audience. Minhag and the chosen posek remain separate: a different practical conclusion must have a basis in the applicable sources. The eight profiles also include Out-of-Town Yeshivish, Torah im Derech Eretz, Dati Leumi, and Chassidish.

For AI Torah learning, Posek prepares divrei Torah, vortlach, derashos, shiur outlines, and source sheets. A kushya must hold up in the context of the pesukim, sugya, or mefarshim. Posek develops the argument from there and distinguishes the source’s own explanation from a proposed chiddush. Bring an existing draft for revision: it checks attributions and strengthens the argument before polishing the language. Generalities that do not follow from the text are cut. Practical shailos have a separate seder for deciding what follows l’maaseh from the facts and verified sources available.

## Release announcement

Posek is an Orthodox AI Rabbi for Torah and Halacha: an open-source skill for source-based halakhah and practical shailos.

Posek prepares teshuvos with exact references to the Shulchan Aruch, Rema, and relevant later poskim. Each answer should make the reasoning clear: which facts control the din, what the sources establish, where the poskim differ, and why the conclusion follows. Both a heter and an issur require a basis in the sources.

The repository includes the skill, source-retrieval tools, a source-verification method, 24 practical halacha development cases, and ten divrei Torah editorial cases. An initial AI-reviewed psak pilot tested nine selected cases: Posek and the baseline each passed all nine. This does not establish an improvement over the baseline, performance on unseen shailos, or rabbinic validation. The [psak evaluation](../benchmarks/RESULTS.md) and [divrei Torah examples and review](../benchmarks/divrei-torah/RESULTS.md) preserve actual outputs and their limits.

Posek is experimental AI software. It can make mistakes in reading or applying a source. Personal status, binding adjudication, and other consequential matters require appropriate qualified judgment. It carries no claim of ordination, communal appointment, or rabbinic endorsement.

Contributions are welcome: corrected mareh mekomos, clearer analysis, difficult shailos, and careful review by people qualified in the relevant area of halacha.

Repository: [frum-compatible/posek](https://github.com/frum-compatible/posek)

Install with:

```sh
npx skills add frum-compatible/posek --skill posek --agent claude-code --agent codex
```

## WhatsApp introduction

Use the deployed phone-page URL after checking its live preview. The page supplies this caption automatically:

> Posek AI — An Orthodox AI Rabbi. Hashkafah: configurable. Mareh mekomos: required. Mutar is also a psak.

The [phone and WhatsApp guide](PHONE-SHARING.md) covers publication. A recipient can read a sample vort and prepare a starter prompt on their phone before deciding whether to install the complete skill.
