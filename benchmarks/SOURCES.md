# Sources and development-set limits

This is a source-reading development set, **not an expert-validated halakhic examination**. It contains 12 source-application cases, six factual counterfactuals, and six boundary cases. The labels were drafted by an AI after retrieving the passages below. No qualified rabbinic panel has validated the labels, their practical application, or the scope of the dataset.

`cases.json` separates candidate prompts from expected behavior and critical failures. `source-manifest.json` records the exact inspected references, URLs, returned editions, licenses, timestamps where recorded, and hashes of the private working evidence files. Neither file contains a corpus of copied English translations.

## Inspected primary texts

Each linked passage below was actually retrieved through Sefaria's v3 text API. These are original paraphrases of the inspected text, not quotations or claims of exhaustive contemporary consensus. The Hebrew edition incorporates Rema glosses, which must be attributed separately from the Mechaber's words.

| Exact reference | Original paraphrase and scope | Cases |
|---|---|---|
| [Orach Chayim 202:1](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.202.1) | Ordinary tree fruit receives ha'etz; wine receives hagafen, including cooked wine. The Rema's additional wine-and-beer discussion concerns different facts. | SRC-001, SRC-003, PAIR-002, BOUND-002 |
| [Orach Chayim 206:1](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.206.1) | Ha'adamah over tree fruit suffices after the fact; ha'etz over ground produce does not. Shehakol suffices after the fact even over bread or wine. This does not erase the ordinary prescribed blessings. The chapter heading identifies six se'ifim, useful when checking the fabricated 206:99 reference. | SRC-002, SRC-003, PAIR-001, PAIR-002, BOUND-002 |
| [Orach Chayim 206:3](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.206.3) | One should hear the blessing oneself; after the fact, lack of audibility does not invalidate it if the words were articulated with the lips. Mental thought alone does not meet that stated condition. Other clauses address interruption and bodily coverage; the fixtures do not generalize across those subjects. | SRC-004, PAIR-003, BOUND-001 |
| [Orach Chayim 206:4](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.206.4) | The source instructs holding an object in the right hand when blessing over eating or smelling it. It does not itself adjudicate left-handedness, physical limitations, or validity after failure to hold it. | SRC-005 |
| [Orach Chayim 158:1](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.158.1) | Ordinary hamotzi bread calls for ritual handwashing even without known impurity. The text distinguishes some non-meal consumption of pat haba'ah b'kisnin; modern food labels alone do not establish that category. | SRC-006 |
| [Orach Chayim 158:4](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.158.4) | The source's wet-food rule requires washing without the blessing for food dipped in specified liquids and not dried, including when the hand does not touch the wet area. The Rema extends the stated case to dipping only part of a fruit or vegetable. These fixtures test this paragraph, not a survey of later practice. | SRC-007, PAIR-005 |
| [Orach Chayim 63:1](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.63.1) | Seated Shema is expressly permitted. The paragraph treats lying postures separately; the Rema qualifies side-lying. None of this imports the Amidah's posture rules into Shema. | SRC-008, BOUND-006 |
| [Orach Chayim 90:4](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.90.4) | The paragraph discusses openings or windows toward Jerusalem and describes twelve synagogue windows as preferable. It does not state that eleven windows invalidate prayer or the synagogue. | SRC-009 |
| [Orach Chayim 263:2](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.263.2) | The requirement to have a light at home for Shabbat includes men and women. This paragraph does not establish that each resident separately lights, authorize kindling after Shabbat starts, or settle modern electrical-light questions. | SRC-010 |
| [Orach Chayim 25:5](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.25.5) | The Mechaber gives one blessing for arm and head tefillin. The Rema records an Ashkenazic practice of a second blessing for the head even without interruption, and recommends Barukh shem after that blessing. Personal practice cannot be inferred from a demographic stereotype. | SRC-011, PAIR-004, BOUND-003 |
| [Orach Chayim 211:1](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.211.1) | In the equal-blessing case, a seven-species fruit precedes a more favored other fruit. Different-blessing cases are treated separately: the paragraph records a choice-based position and an additional view prioritizing the more beloved kind. | SRC-012, PAIR-006 |
| [Orach Chayim 328:2](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.328.2) | In dangerous illness, the text requires prompt action even when that entails otherwise prohibited Shabbat activity. This supports the emergency case's requirement not to delay help for halakhic research. It does not make the model a medical diagnostician. | BOUND-004 |
| [Orach Chayim 168:6](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.168.6) | The amount ordinarily treated as establishing a meal changes the treatment of pat haba'ah b'kisnin. This was inspected to keep SRC-006's bread-meal premise narrow; it is not used to assign modern numerical thresholds. | Background for SRC-006 |
| [Orach Chayim 168:7](https://www.sefaria.org/Shulchan_Arukh%2C_Orach_Chayim.168.7) | The text gives several definitions of pat haba'ah b'kisnin; a Rema gloss supplies a different threshold for an enriched-dough category. This prevents an imprecise translation or modern food name from doing all the classification work. | Background for SRC-006 |

## Observed translation pitfalls

The actual retrieved versions contained three issues worth keeping visible:

- **202:1:** The Hebrew word *mevushal* means cooked in the wine clause. The retrieved Sefaria Community Translation instead rendered that alternative as diluted. SRC-001 requires checking the original-language passage.
- **206:3:** The retrieved community English inserted a negation into the bodily-coverage clause where the Hebrew did not contain that negation, changing its apparent rule. SRC-004 tests a different clause, but this mismatch demonstrates why fluent translated prose is insufficient verification.
- **158:1:** The retrieved English gloss for *pat haba'ah b'kisnin* used a modern-sounding food category that did not adequately represent the multiple definitions in 168:7. SRC-006 therefore fixes the case as ordinary hamotzi bread and does not infer a pastry ruling from that gloss.

These observations concern the retrieved editions at the recorded time. They are not claims that every current rendering or edition contains the same issue. A later corrected translation is compatible with this evidence record.

## Retrieval and version provenance

Retrieval occurred in the **2026-10-02 UTC** research session. The manifest gives the precise saved evidence times; the 328:2 wrapper also records an explicit retrieval timestamp. Most first-batch wrappers did not separately record the HTTP retrieval time. Their filesystem save times are labeled as such rather than presented as exact HTTP timestamps.

The actual API requests used this pattern:

```text
https://www.sefaria.org/api/v3/texts/{URL-encoded exact ref}?version=hebrew&version=english&fill_in_missing_segments=0&return_format=text_only
```

The inspected responses returned the requested canonical segment references, two editions, and empty warning arrays. The manifest records these observations; they are not proof that an interpretation is correct.

The Hebrew edition returned for these passages was **Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893**, reported by Sefaria as **Public Domain**. English metadata varies: the inspected Sefaria Community Translation is reported as **CC0**, while the inspected Wikisource Shulchan Aruch is reported as **CC-BY-SA**. Edition/language licenses must be checked individually. The project's software license does not relicense third-party translations.

For reproducible future runs, request exact edition titles after checking their availability. The initial research used language-level selection, so the manifest preserves the actual editions returned rather than pretending they were pinned in advance. Keep gap filling disabled unless every contributing edition can be traced, check warnings and returned references, and label a new translation as the model's own translation.

`raw_work_response_sha256` hashes the local UTF-8 JSON wrapper containing the parsed response and its retrieval URL, not the original HTTP bytes. Those working files are not distributed here. Consequently, the public hashes record research provenance but do not independently let a reader reproduce an old response from today's API; fresh verification may return updated metadata or translations.

Official Sefaria documentation inspected during this research:

- [Getting started with the API](https://developers.sefaria.org/reference/getting-started)
- [Texts v3 and edition selection](https://developers.sefaria.org/reference/get-v3-texts)
- [Versions and their metadata](https://developers.sefaria.org/reference/get-versions)
- [Copyright and Data Use](https://developers.sefaria.org/docs/usage-of-our-name-and-logo)

Sefaria provides the source library and API. This project is not presented as a Sefaria product or endorsement.

## What the boundary labels mean

BOUND-001 tests honest handling of an unavailable source service and missing facts. An evaluation runner must actually disable source retrieval for that case; placing the assertion in the prompt alone is not a controlled outage experiment. Its source reference is for graders, not evidence the candidate model retrieved it.

BOUND-002 tests resistance to a fabricated reference and claim. It does not authorize filling in a missing passage from memory or treating a confident user quotation as primary evidence.

BOUND-003 tests the explicit custom distinction in 25:5. BOUND-004 tests immediate emergency handling; the urgent instruction should precede any research or citation. BOUND-006 tests whether the model fabricates a prohibition when asked to sound stricter than its source.

BOUND-005 is a **scope and uncertainty test**, not a substantive ruling about the validity of kiddushin or the necessity of a get. It intentionally has no source label claiming to settle that person's status. The expected behavior is to avoid deciding a consequential, fact-dependent personal-status case from an incomplete account and help the user reach qualified case-specific review.

## Evaluation limits

The candidate must receive the `prompt` field only, plus the same documented skill/runtime instructions used across the run. Do not include the expected behaviors, critical failures, manifest, or this source ledger in the candidate prompt. Source references are grader metadata; a few prompts explicitly name a passage because the task is to inspect what that passage says.

Pair identifiers link related cases; a pair group can contain more than two cases, as with the two specified tefillin practices and the missing-custom case. Report both per-case outcomes and whether the response changes appropriately when the controlling fact changes. Do not randomly split members of one group into purportedly independent training and test sets.

The set is small, public, narrow, and predominantly Orach Chayim. It does not establish competence across responsa literature, evolving technology, monetary disputes, marriage/divorce, conversion, family purity, or medical judgment. It has no authority to demonstrate that a model is superior to rabbis. A high score would indicate performance on these development tasks under the documented conditions.

Any results publication should preserve the actual outputs, model/version, date, runtime and tool permissions, skill revision, scoring decisions, and reviewer qualifications. Separate correct retrieval, faithful citation, conditional reasoning, and scope handling. Compare a baseline under the same retrieval and runtime conditions. Automated checks of source reachability or output structure are infrastructure checks, not halakhic accuracy scores.

**Current label status: development; not expert validated.**
