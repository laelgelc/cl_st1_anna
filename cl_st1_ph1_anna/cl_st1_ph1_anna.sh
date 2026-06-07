# Tag the corpus.
python tag.py
# Produces: corpus/07_tagged

# Extract key lemmas from the tagged corpus.
# Only lemmas with frequency >= 3 are retained.
python keylemmas.py \
    --input corpus/07_tagged \
    --output corpus/08_keylemmas \
    --cutoff 3
# Produces: corpus/08_keylemmas

# Select keywords from the key-lemma files using stratified selection.
python select_kws_stratified.py \
    --input-dir corpus/08_keylemmas \
    --output-dir corpus/09_kw_selected
# Produces: corpus/09_kw_selected

# ----------------------------------------------------------------------
# Keyword-selection reference output
# ----------------------------------------------------------------------

# Case 1: Paragraphs shorter than 10 words are kept.
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

# Case 2: Paragraphs shorter than 10 words are removed.
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

# ----------------------------------------------------------------------
# Column generation and SAS preparation
# ----------------------------------------------------------------------

# Remove previously generated column directories before rebuilding them.
rm -rf columns columns_clean

# Generate keyword-count columns and related index files.
python columns.py
# Produces: columns, columns_clean, file_ids.txt, index_keywords.txt

# Merge generated columns into a SAS-compatible counts file.
python merge_columns.py
# Produces: sas/counts.txt

# Generate SAS format files, such as word-label formats.
python sas_formats.py
# Produces: sas/word_labels_format.sas, etc.

# ----------------------------------------------------------------------
# Manual SAS step
# ----------------------------------------------------------------------

# Run the SAS analysis manually.
# Use Rogerio Yamada's account.

# ----------------------------------------------------------------------
# Post-SAS analysis and reporting
# ----------------------------------------------------------------------

# Generate factor lists from the SAS output.
python factor_lists.py
# Produces: factors

# Calculate corpus-size statistics.
python corpus_size.py
# Produces: corpus_size/corpus_size.tsv

# Build LaTeX boxplot slides for the factor analysis.
cd latex_boxplots
python latex_boxplots.py
# Produces: latex_boxplots/slides
cd ..

# Generate LaTeX ANOVA tables.
python latex_anova_table.py
# Produces: latex_tables

# Generate examples in LaTeX format.
python examples.py
# Produces: examples

# Run a sanity check on the scores.
python score_details.py
# Produces: examples/score_details.txt

# Generate examples in plaintext format.
python examples_txt.py
# Produces: examples_txt