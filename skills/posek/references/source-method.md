# Source method

## Choose the right starting text

For a practical shailah, trace the applicable halachic authorities. For a dvar Torah or textual explanation, begin with the passage being discussed: the pesukim in context, the actual sugya or Midrash, and the relevant mefaresh. Do not force a Shulchan Aruch citation into a literary or aggadic question. Read enough surrounding text to distinguish a question from an answer, a rejected view from the conclusion, and a reported interpretation from an author's own position.

The helper below also retrieves exact segments of Tanach, Rashi, Mishnah, Gemara, and Rambam when their canonical Sefaria references are supplied. Find the actual reference structure instead of guessing it: a commentary may require its own segment number, and a daf can contain many segments. Use the source's own spelling in tool arguments even when the prose uses familiar yeshivish transliteration.

## Find a rule without inventing an authority

Start with the question's controlling facts, then search for the relevant primary text. Search snippets, shiur notes, and Q&A summaries can locate an authority; they do not replace reading it. Where the question concerns a particular community or living posek, use a verifiable publication from that authority. Identify uncertainty about attribution or edition.

The four Shulchan Arukh divisions are Orach Chayim (daily practice, Shabbat, festivals), Yoreh De'ah (including kashrut and other ritual law), Even HaEzer (marriage and related personal status), and Choshen Mishpat (civil law). Select a specific siman and se'if rather than citing an entire division.

The Mechaber's text and the Rema's gloss may share one digital segment. In Hebrew, הגה commonly marks the gloss. Do not attribute the Rema's practice to the Mechaber or assume every gloss is a universal Ashkenazic instruction. Later rulings and actual communal practice can be decisive.

## Retrieve an exact segment

With a shell and Python 3.10 or later available, run the bundled helper, using its actual installed path:

```sh
python3 scripts/fetch_source.py 'Shulchan Arukh, Orach Chayim 202:1'
```

Run that command from this skill's folder, or use an absolute path to the script. An optional `--output PATH` writes an evidence record. Use a scratch directory outside a public repository for retrieved text and private questions. The helper needs outbound HTTPS to Sefaria but no API key and no third-party Python packages.

It requests the original language and English from the [Sefaria v3 text API](https://developers.sefaria.org/reference/get-v3-texts), disables filling missing segments, and records the canonical locator, edition metadata, retrieval time, warnings, and raw-response hash. It rejects non-segment or silently changed references; discover the canonical title through the library before retrying. A missing English translation is explicit. A hash is a retrieval audit aid, not proof of correct interpretation or immutable textual authority.

For a commentary or edition not returned by the helper, use the browsing tool or an appropriate documented API request and record the actual edition read. Retrieve adjacent segments separately when context matters. Never claim that the helper searched the literature. It retrieves the segment supplied to it.

No shell or no network: use browser-accessible primary texts or the user's excerpt. If neither is available, give only appropriately labeled background and say what evidence is needed. Do not make up a successful tool call.

## Read before quoting

Maintain a small evidence ledger while researching:

| Claim | Exact locator and speaker | Evidence inspected | Scope / unresolved issue |
| --- | --- | --- | --- |
| The proposition this source supports | Division, siman, se'if; Mechaber/Rema/commentator | Link or supplied passage; edition when relevant | Conditions, translation problem, later authority needed |

Use the ledger to write the response; do not require the user to read research logs. Read adjacent se'ifim when the extracted sentence depends on them. A source saying one thing about a food before eating may say something different about an erroneous blessing after the fact.

Compare the decisive Hebrew wording with translations, especially negation, food categories, quantities, and statements of obligation versus preference. If originals and translations conflict and you cannot resolve the conflict, report it rather than silently choosing the convenient reading.

When naming a commentary's dibbur hamaschil, inspect that exact comment. A page that runs adjacent comments together can attach the right argument to the wrong heading. If only the broader page is verified, cite that page and omit an unverified narrower heading.

Do not flatten halakhic disagreement into a numerical confidence score. Report separately whether the text was verified, its interpretation is clear, facts are established, and the relevant practice is known. Precision in one does not imply certainty in the others.

## Text rights and provenance

Sefaria is a host, not one blanket license. Translations and editions have different rights. Inspect the returned version's license and source fields; preserve required attribution when distributing excerpts. Missing metadata is not permission. Prefer links and original paraphrases. Do not bundle an entire translation into this skill. The project's MIT license covers its own material, not independently retrieved texts. See [Sefaria's Copyright and Data Use guidance](https://developers.sefaria.org/docs/usage-of-our-name-and-logo).
