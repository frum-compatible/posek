# Semicha-question pilot

The pilot tests Posek and a no-skill assistant on four public examination-related items. It does not administer a full semicha examination or compare either condition with human candidates.

## Frozen selection

[questions.json](questions.json) preserves the prompts, original links, and question locations. Selection preceded candidate generation: the first three numbered content questions from one Chief Rabbinate Issur veHeter paper, plus the one authenticated WebYeshiva midterm item located in a bounded search. Every selected question remains in the report regardless of its result.

The Chief Rabbinate subset includes all subparts. The paper contains twelve questions and requires candidates to answer seven of eight study questions and three of four application questions. The inspected instructions do not specify duration or reference-material permissions. This pilot uses condensed English paraphrases and permits source access; it does not reproduce the original conditions.

The WebYeshiva instructor announced the selected item as a planned midterm question and invited early submissions. This is not a complete administered paper; final wording, marking rules, and pass threshold are unverified. The adaptation adds the shared request for citations.

A bounded search of official YU/RIETS resources found program requirements and review material, but no authenticated public semicha paper. No item is labeled a YU examination. This is a search limitation, not proof that no public paper exists.

## Candidate conditions

Each question receives two fresh sessions: one with the frozen Posek bundle and one general assistant instructed not to load a domain skill. Both may browse primary sources and use the same standalone source helper. They receive the same question, an English answer request, a target of 1,800 words, and a requested research cap of ten minutes. The time cap is an instruction, not a runtime-enforced limit.

Candidates are instructed not to read grading material, previous answers, or another candidate's work. They share a filesystem; isolation is instructional rather than an operating-system boundary. The runtime may expose installed-skill descriptions even when a baseline does not load the skill. Save original answers and actual retrieval notes, including failures. No retry may replace an inconvenient result.

The [input manifest](input-manifest.json) records the frozen skill hashes and rubric. Candidate runtimes inherit the same parent without model overrides, but exact model identifiers and generation settings are not exposed. There is one run per question per condition.

## Independent review

A fresh AI reviewer receives opaque response IDs without the condition mapping. Answer wording may reveal the condition, so the presentation is only partially blinded. The reviewer checks primary sources, every requested subpart, and the six dimensions fixed in the manifest: conclusion, source fidelity, attribution, minhag and scope, uncertainty, and usefulness.

Each dimension receives 0, 1, or 2. The development pass rule is at least 10 of 12 points, no zero dimension, and no critical failure. Critical failures include invented decisive sources, false verification, materially wrong controlling conclusions, and erased controlling exceptions. Missing subparts and unresolved citations must be listed. These thresholds are the project's rubric; they are not an institution's marking scheme.

Preserve review disagreements and corrections with their reasons. Report both conditions, answer hashes, every question result, and retrieval failures. No qualified human examiner has graded this pilot.

## What a result can establish

This can show how the recorded assistants handled these four adapted public items under source-assisted conditions. A public question may have appeared in model training. Withholding answers from a fresh session does not make the material demonstrably unseen to the model.

Neither a high rubric score nor a tie establishes an official pass, semicha, a candidate percentile, or superiority to rabbonim. A percentile requires an appropriate candidate-score distribution. A comparison with practicing rabbonim requires actual participants and independent qualified grading; see the [separate proposed study](../RABBI-COMPARISON.md).
