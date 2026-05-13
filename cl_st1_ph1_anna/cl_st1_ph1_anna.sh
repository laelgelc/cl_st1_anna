python tag.py
# Output: corpus/07_tagged

python keylemmas.py \
    --input corpus/07_tagged \
    --output corpus/08_keylemmas \
    --cutoff 3

python select_kws_stratified.py \
    --input-dir corpus/08_keylemmas \
    --output-dir corpus/09_kw_selected
# Output: corpus/09_kw_selected

# Case 1 (without removing paragraphs shorter than 10 words)
"
Reading key-lemma files from: corpus/08_keylemmas
  es                   → loaded 36 POSKW lemmas (after filtering)
  mg                   → loaded 54 POSKW lemmas (after filtering)
  rj                   → loaded 52 POSKW lemmas (after filtering)
  sp                   → loaded 28 POSKW lemmas (after filtering)

=== Keyword Summary ===
Total POSKW lemmas (incl. duplicates): 170
Unique POSKW lemmas:                  168
Duplicates removed in consolidated:   2
=======================

Wrote    36 lemmas → corpus/09_kw_selected/es.txt
Wrote    54 lemmas → corpus/09_kw_selected/mg.txt
Wrote    52 lemmas → corpus/09_kw_selected/rj.txt
Wrote    28 lemmas → corpus/09_kw_selected/sp.txt

Final unique keywords written: 168 → corpus/09_kw_selected/keywords.txt
"
# Case 2 (removing paragraphs shorter than 10 words)
"
Reading key-lemma files from: corpus/08_keylemmas
  es                   → loaded 38 POSKW lemmas (after filtering)
  mg                   → loaded 52 POSKW lemmas (after filtering)
  rj                   → loaded 51 POSKW lemmas (after filtering)
  sp                   → loaded 27 POSKW lemmas (after filtering)

=== Keyword Summary ===
Total POSKW lemmas (incl. duplicates): 168
Unique POSKW lemmas:                  166
Duplicates removed in consolidated:   2
=======================

Wrote    38 lemmas → corpus/09_kw_selected/es.txt
Wrote    52 lemmas → corpus/09_kw_selected/mg.txt
Wrote    51 lemmas → corpus/09_kw_selected/rj.txt
Wrote    27 lemmas → corpus/09_kw_selected/sp.txt

Final unique keywords written: 166 → corpus/09_kw_selected/keywords.txt
"

rm -rf columns columns_clean
python columns.py
# Output: columns, columns_clean, file_ids.txt, index_keywords.txt

python merge_columns.py
# Output: sas/counts.txt

python sas_formats.py
# Output: sas/word_labels_format.sas, etc

## RUN SAS
## Rogerio Yamada's account

python factor_lists.py
# Output: factors

python corpus_size.py
# Output: corpus_size/corpus_size.tsv

python examples.py
# Output: examples (LaTeX format)

# Sanity check on the scores:
python score_details.py
# Output: examples/score_details.txt

python examples_txt.py
# Output: examples_txt (plaintext format)
