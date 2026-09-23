# Corpus Linguistics - Study 1 - Anna

## Phase 0 - PDF scraping

- 97 of the 101 PDF documents were scraped
- The following documents were image-based PDFs and could not be scraped:
    - AM_Infantil - cópia.pdf
    - AM_EM.pdf
    - AM_Fundamental II.pdf
    - AM_Fundamental I.pdf

## Phase 1 - Pilot Lexical Multi-dimensional Analysis

### Data wrangling

The EF Sudeste pilot curriculum documents were cleaned and transformed into a paragraph-level corpus suitable for quantitative analysis.

1. **Filename normalization**

- All `.txt` files in `corpus/00_source_ef_sudeste_pilot` were renamed to a consistent format:
    - Converted to lowercase.
    - Spaces replaced with underscores.
    - Multiple consecutive underscores collapsed into a single underscore.
- This ensures stable, machine-readable identifiers across all subsequent steps.

2. **Paragraph normalization**

- Each source file was line-processed so that:
    - Consecutive non-empty lines were joined into a single paragraph.
    - Paragraphs were separated by a single blank line.
- The normalized versions overwrote the originals in `corpus/00_source_ef_sudeste_pilot`, so each file now consists of well-defined paragraph blocks.

3. **File-level metadata**

- A DataFrame (`source_ef_sudeste_pilot_df`) was created with one row per source file and the following fields:
    - `filename`: normalized filename.
    - `state`: state code inferred from the filename prefix (`es`, `mg`, `rj`, `sp`).
- File counts and percentages per state were computed to summarize the distribution of documents.

4. **Paragraph-level dataset**

- For each source file, paragraphs were extracted by splitting on blank lines.
- For every paragraph, the following information was recorded:
    - `filename`: original file it came from.
    - `state`: state code of the source file.
    - `paragraph_index`: 1-based index of the paragraph within the file.
    - `filename_paragraph`: derived name in the format `<filename>_p<index>.txt`.
    - `word_count`: number of whitespace-separated tokens in the paragraph.
- This produced a paragraph-level DataFrame (`source_ef_sudeste_pilot_paragraph_df`) with 2,394 paragraphs.

5. **Descriptive statistics and outlier detection**

- Descriptive statistics for `word_count` (mean, standard deviation, quartiles, min/max) were computed.
- An IQR-based rule was used to flag length outliers:
    - `lower_bound = Q1 - 1.5 * IQR`
    - `upper_bound = Q3 + 1.5 * IQR`
- Paragraphs with `word_count` outside `[lower_bound, upper_bound]` were labeled as outliers.
- Out of 2,394 paragraphs, 106 (≈4.43%) were flagged as outliers and 2,288 as non-outliers.

6. **Export of paragraph-level data**

- The complete paragraph-level DataFrame (including the `outlier` flag) was exported as NDJSON to:
    - `corpus/source_ef_sudeste_pilot_paragraph.ndjson`
- Each line is a UTF-8 JSON record, oriented to support streaming and downstream processing.

7. **Creation of a per-paragraph, per-state corpus**

- A directory `corpus/02_extracted` was created with one subdirectory per state:
    - `corpus/02_extracted/es`
    - `corpus/02_extracted/mg`
    - `corpus/02_extracted/rj`
    - `corpus/02_extracted/sp`
- For each non-outlier paragraph, a standalone `.txt` file was written:
    - The file name is `filename_paragraph` (e.g. `sp_inf_e_ef_intro_9_p7.txt`).
    - Files are stored in the subdirectory corresponding to their state.
- This results in 2,288 paragraph files.

8. **Filtering very short paragraphs**

- The paragraph-level NDJSON file (`corpus/source_ef_sudeste_pilot_paragraph.ndjson`) was reloaded and augmented with a new boolean flag:
    - `shorter_than_10_words`: `True` if `word_count` < 10, `False` otherwise.
- A total of 17 paragraphs were identified as having fewer than 10 words.
- The updated DataFrame, including `shorter_than_10_words`, was written back to:
    - `corpus/source_ef_sudeste_pilot_paragraph.ndjson`
- All corresponding paragraph files with `word_count` < 10 were then removed from the per-state corpus:
    - Deleted from `corpus/02_extracted/<state>/<filename_paragraph>`.
    - Deleted from `corpus/07_tagged/<state>/<filename_paragraph>` when present.
- After this filtering step, the per-state extracted and tagged corpora no longer contain paragraphs shorter than 10 words, reducing noise from extremely short segments in subsequent analyses.
- This results in 2,271 paragraph files distributed across the four state-specific subdirectories, providing a cleaned, state-organized paragraph corpus ready for lexical multi-dimensional analyses.

### Lexical Multi-dimensional Analysis

- The Lexical Multi-dimensional Analysis (LMDA) was processed according to the corresponding procedures.

## Phase 2 - Lexical Multi-dimensional Analysis

Phase 2 extends the Lexical Multi-dimensional Analysis to the full Brazilian educational curriculum and guideline corpus. The texts were denoised, organised by state-level strata, tagged, transformed into lexical variables, and analysed through the LMDA workflow.

### Corpus preparation and denoising

- The source corpus was prepared from Brazilian educational curriculum and guideline excerpts.
- LLM-based denoising was applied to remove noise while preserving the relevant curriculum/guideline content.
- The denoised corpus was written to:
    - `cl_st1_ph2_anna/corpus/02_extracted`
- Files requiring reprocessing were handled individually when the first denoising output was incomplete or invalid.

### Tagging and lexical variable construction

- The denoised corpus was tagged and grouped by state.
- Tagged outputs were written to:
    - `cl_st1_ph2_anna/corpus/07_tagged/<state>/`
- Key lemmas were extracted from the tagged corpus by state.
- A stratified keyword selection procedure was used to balance lexical representation across states:
    - Up to 45 keywords were selected per state.
    - 1,198 candidate keywords were consolidated before de-duplication.
    - 1,061 unique keywords were retained after removing duplicates.
- The final selected keyword list was written to:
    - `cl_st1_ph2_anna/corpus/09_kw_selected/keywords.txt`

### SAS input preparation

- Binary keyword columns were generated for each text using the final selected keyword list.
- The generated files include:
    - `cl_st1_ph2_anna/columns/`
    - `cl_st1_ph2_anna/columns_clean/`
    - `cl_st1_ph2_anna/file_ids.txt`
    - `cl_st1_ph2_anna/index_keywords.txt`
- The keyword columns were merged into the SAS counts matrix:
    - `cl_st1_ph2_anna/sas/counts.txt`
- SAS format files were generated to map variable IDs to readable keyword labels.

### Lexical Multi-dimensional Analysis

- The SAS-based LMDA workflow was run externally using the generated counts matrix and format files.
- The SAS workflow produced factor-score, loading, ANOVA, and parameter outputs.
- Post-SAS scripts generated:
    - Factor loading lists in `cl_st1_ph2_anna/factors/`
    - Corpus-size summaries in `cl_st1_ph2_anna/corpus_size/`
    - LaTeX/TikZ boxplots in `cl_st1_ph2_anna/latex_boxplots/slides/`
    - ANOVA tables in `cl_st1_ph2_anna/latex_tables/`
    - Representative factor-pole examples in `cl_st1_ph2_anna/examples/`
    - Plain-text example extracts in `cl_st1_ph2_anna/examples_txt/`
    - Score-detail reports in `cl_st1_ph2_anna/examples/score_details.txt`

### Interpretation materials

- Interpretation prompts were generated by combining:
    - Factor loading lists.
    - Factor score summaries.
    - Representative examples.
    - Score-detail information.
- Prompt files were written to:
    - `cl_st1_ph2_anna/interpretation/input/`
- GPT-generated interpretation outputs were written to:
    - `cl_st1_ph2_anna/interpretation/output/`

### Pipeline documentation

Detailed Phase 2 command history and pipeline documentation are available in:

- `cl_st1_ph2_anna/cl_st1_ph2_anna_pipeline.md`
- `cl_st1_ph2_anna/cl_st1_ph2_anna_pipeline_description.md`
