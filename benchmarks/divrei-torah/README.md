# Divrei Torah development cases

Ten public development cases assess whether Posek can prepare and revise useful divrei Torah with faithful sources, a genuine argument, and appropriate delivery. These cases are separate from the 24-case practical halachah suite. They do not measure competence to issue psak, and their answer criteria are not halachic authority.

The set contains two ordinary generation requests and eight adversarial or revision requests. It targets invented kushyos, decorative sources, erased disagreement, unverified quotations, false attribution of a chiddush, inflated conclusions, empty prose, and the misuse of a vort as a heter. The [initial four-case examples and review](RESULTS.md) preserve actual outputs; they are not a result for the whole suite.

## Run without leaking the rubric

1. Start a fresh candidate session with the skill and one case's `prompt` only. Do not include this README, `review_checks`, `critical_failures`, previous answers, or evaluator notes in the candidate context.
2. Preserve the complete answer and available source/tool evidence. Record the case ID, exact model identifier when available, skill version or hash, date, host, available tools, and retrieval failures. Source access failures must remain visible.
3. Give a separate reviewer the prompt, answer, evidence, and rubric. Verify source-specific judgments against primary text; a rubric is not a substitute for reading the source. Record the reviewer's qualifications, including when the reviewer is another AI.
4. For a comparison, run the same prompts without the skill under equivalent model, tool, and generation settings. Keep answers blinded and randomize their order for editorial review. Public development cases are not an unseen test set.

## Separate source failures from editorial judgment

Record each listed critical failure as present, absent, or unresolved, with the relevant output excerpt and supporting evidence. Fabricated sources, material misattribution, material misrepresentation, false retrieval claims, and unsupported practical rulings cannot be offset by elegant writing. If source evidence is unavailable, mark the judgment unresolved rather than assuming correctness.

Then assess the `review_checks` with short evidence-based notes. Focus on whether the piece has a real interpretive point, whether the source supports the claim, whether the payoff follows from that reasoning, and whether the piece serves the requested audience and length. Honor harmless user preferences; editorial taste is not permission to override them. A familiar idea can be excellent when it is developed clearly and faithfully.

For a spoken-word cap, evaluate only the visibly separated spoken text, excluding source notes. A requested delivery time is approximate and depends on the speaker, pauses, and Hebrew reading. If reporting word counts, state the counting convention and use it consistently across candidates.

Report factual failures and unresolved source checks separately from editorial strengths, weaknesses, or blinded preferences. Preserve answers and review evidence. Do not convert prose ratings into a claim of halachic accuracy, invent a percentage, or claim expert validation without qualified independent review. Any eventual report should identify the cases run, sample size, omissions, evaluator limits, and whether a comparison actually showed improvement.
