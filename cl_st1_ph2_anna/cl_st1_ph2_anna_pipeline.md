# Corpus Linguistics - Study 1 - Phase 2 - Anna

Run the commands from the project phase directory, e.g.:

```text
cl_st1_ph2_anna/
```

## 1. Denoise the guideline excerpts

### Dry run

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --limit 10 \
    --max-output-tokens 10000 \
    --dry-run
```


### Test run, first time

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --limit 10 \
    --max-output-tokens 10000
```

### 10 workers test run

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --limit 200 \
    --workers 10 \
    --resume \
    --max-output-tokens 10000
```

### Full run

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --workers 10 \
    --resume \
    --max-output-tokens 10000 \
    --max-retries 5
```

### Production mode on an EC2 instance

```shell
bash run_python_ec2.sh \
    llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --workers 10 \
    --resume \
    --max-output-tokens 10000 \
    --max-retries 5
```

### Retry specific files

`se_inf_1.txt` was initially flagged as `error`. A try switched it to `success`, but the output file was incomplete.

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --max-output-tokens 10000 \
    --max-retries 5 \
    --only-filename se_inf_1.txt \
    --reprocess
```

The `llm_denoise.py` programme was extended with Gemini support. It was run with the `--model` flag set to `gemini-3.8-flash`. This time, the output file was correctly generated.

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gemini-3.8-flash \
    --max-output-tokens 10000 \
    --max-retries 5 \
    --only-filename se_inf_1.txt \
    --reprocess
```

`ms_inf_e_ef_45.txt` was initially flagged as `invalid`. The `llm_denoise.py` programme was adjusted with less restrictive `refusal_patterns`. After a rerun, the output file was correctly generated.

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v2.md \
    --model gpt-6-luna \
    --max-output-tokens 10000 \
    --max-retries 5 \
    --only-filename ms_inf_e_ef_45.txt \
    --reprocess
```

## 2. Tag the corpus

```shell
python tag.py
```

Output: `corpus/07_tagged/<group>/`

## 3. Extract key lemmas by group

```shell
python keylemmas.py \
  --input corpus/07_tagged \
  --output corpus/08_keylemmas \
  --cutoff 3
```

Output: `corpus/06_keylemmas/<group>.tsv`

## 4. Select a stratified keyword set

```shell
python select_kws_stratified.py \
    --per-group 40 \
    --max-total 20000
```

Output: `corpus/07_kw_selected/keywords.txt

```shell
=== Group Keyword Quotas ===
global_north_2023_09   → 40 keywords max
global_north_2023_10   → 40 keywords max
global_north_2023_11   → 40 keywords max
global_north_2023_12   → 40 keywords max
global_north_2024_01   → 40 keywords max
global_north_2024_02   → 40 keywords max
global_north_2024_03   → 40 keywords max
global_north_2024_04   → 40 keywords max
global_north_2024_05   → 40 keywords max
global_north_2024_06   → 40 keywords max
global_north_2024_07   → 40 keywords max
global_north_2024_08   → 40 keywords max
global_north_2024_09   → 40 keywords max
global_north_2024_10   → 40 keywords max
global_north_2024_11   → 40 keywords max
global_north_2024_12   → 40 keywords max
global_north_2025_01   → 40 keywords max
global_north_2025_02   → 40 keywords max
global_north_2025_03   → 40 keywords max
global_north_2025_04   → 40 keywords max
global_north_2025_05   → 40 keywords max
global_north_2025_06   → 40 keywords max
global_south_2023_09   → 40 keywords max
global_south_2023_10   → 40 keywords max
global_south_2023_11   → 40 keywords max
global_south_2023_12   → 40 keywords max
global_south_2024_01   → 40 keywords max
global_south_2024_02   → 40 keywords max
global_south_2024_03   → 40 keywords max
global_south_2024_04   → 40 keywords max
global_south_2024_05   → 40 keywords max
global_south_2024_06   → 40 keywords max
global_south_2024_07   → 40 keywords max
global_south_2024_08   → 40 keywords max
global_south_2024_09   → 40 keywords max
global_south_2024_10   → 40 keywords max
global_south_2024_11   → 40 keywords max
global_south_2024_12   → 40 keywords max
global_south_2025_01   → 40 keywords max
global_south_2025_02   → 40 keywords max
global_south_2025_03   → 40 keywords max
global_south_2025_04   → 40 keywords max
global_south_2025_05   → 40 keywords max
global_south_2025_06   → 40 keywords max
============================

global_north_2023_09   → selected 40/40 from 455 available POSKW lemmas
global_north_2023_10   → selected 40/40 from 475 available POSKW lemmas
global_north_2023_11   → selected 40/40 from 347 available POSKW lemmas
global_north_2023_12   → selected 40/40 from 342 available POSKW lemmas
global_north_2024_01   → selected 40/40 from 315 available POSKW lemmas
global_north_2024_02   → selected 40/40 from 326 available POSKW lemmas
global_north_2024_03   → selected 40/40 from 380 available POSKW lemmas
global_north_2024_04   → selected 40/40 from 375 available POSKW lemmas
global_north_2024_05   → selected 40/40 from 413 available POSKW lemmas
global_north_2024_06   → selected 40/40 from 307 available POSKW lemmas
global_north_2024_07   → selected 40/40 from 296 available POSKW lemmas
global_north_2024_08   → selected 40/40 from 279 available POSKW lemmas
global_north_2024_09   → selected 40/40 from 289 available POSKW lemmas
global_north_2024_10   → selected 40/40 from 363 available POSKW lemmas
global_north_2024_11   → selected 40/40 from 359 available POSKW lemmas
global_north_2024_12   → selected 40/40 from 308 available POSKW lemmas
global_north_2025_01   → selected 40/40 from 383 available POSKW lemmas
global_north_2025_02   → selected 40/40 from 433 available POSKW lemmas
global_north_2025_03   → selected 40/40 from 425 available POSKW lemmas
global_north_2025_04   → selected 40/40 from 363 available POSKW lemmas
global_north_2025_05   → selected 40/40 from 436 available POSKW lemmas
global_north_2025_06   → selected 40/40 from 477 available POSKW lemmas
global_south_2023_09   → selected 40/40 from 248 available POSKW lemmas
global_south_2023_10   → selected 40/40 from 379 available POSKW lemmas
global_south_2023_11   → selected 40/40 from 301 available POSKW lemmas
global_south_2023_12   → selected 40/40 from 362 available POSKW lemmas
global_south_2024_01   → selected 40/40 from 321 available POSKW lemmas
global_south_2024_02   → selected 40/40 from 237 available POSKW lemmas
global_south_2024_03   → selected 40/40 from 262 available POSKW lemmas
global_south_2024_04   → selected 40/40 from 249 available POSKW lemmas
global_south_2024_05   → selected 40/40 from 250 available POSKW lemmas
global_south_2024_06   → selected 40/40 from 221 available POSKW lemmas
global_south_2024_07   → selected 40/40 from 265 available POSKW lemmas
global_south_2024_08   → selected 40/40 from 334 available POSKW lemmas
global_south_2024_09   → selected 40/40 from 327 available POSKW lemmas
global_south_2024_10   → selected 40/40 from 412 available POSKW lemmas
global_south_2024_11   → selected 40/40 from 346 available POSKW lemmas
global_south_2024_12   → selected 40/40 from 293 available POSKW lemmas
global_south_2025_01   → selected 40/40 from 350 available POSKW lemmas
global_south_2025_02   → selected 40/40 from 387 available POSKW lemmas
global_south_2025_03   → selected 40/40 from 333 available POSKW lemmas
global_south_2025_04   → selected 40/40 from 274 available POSKW lemmas
global_south_2025_05   → selected 40/40 from 368 available POSKW lemmas
global_south_2025_06   → selected 40/40 from 438 available POSKW lemmas

Total consolidated keywords before de-duplication: 1760
Unique keywords after de-duplication: 1041
Duplicates removed: 719

Final unique keywords written to: corpus/07_kw_selected/keywords.txt
Final unique keyword count: 1041
```

## 5. Build binary keyword columns

```shell
rm -rf columns columns_clean
```

```shell
python columns.py
```

Outputs:
- `columns/`
- `columns_clean/`
- `file_ids.txt`
- `index_keywords.txt`

## 6. Merge columns into the SAS counts matrix

```shell
python merge_columns.py
```

Output: `sas/counts.txt`

## 7. Generate SAS format files

```shell
python sas_formats.py
```

Outputs:

- sas/word_labels_format.sas
- sas/word_labels_full_format.sas
- other SAS helper format files

## 8. Run SAS

## 9. Build factor loading lists

```shell
python factor_lists.py
```

Output: factors/

## 10. Calculate corpus size summaries

```shell
python corpus_size.py
```

Output: `corpus_size/corpus_size.tsv`

## 11. Generate LaTeX/TikZ boxplots

```shell
cd latex_boxplots
```

```shell
python latex_boxplots.py
```

Output: `latex_boxplots/slides/`

```shell
cd ..
```

## 12. Generate LaTeX ANOVA table

```shell
python latex_anova_table.py
```

Output: `latex_tables/anova_decade.tex`

## 13. Generate LaTeX example extracts

```shell
python examples.py
```

Output: `examples/`

## 14. Generate score-details report

```shell
python score_details.py
```

Output: `examples/score_details.txt`

## 15. Generate plaintext example extracts

```shell
python examples_txt.py
```

Output: `examples_txt/`

## 16. Build interpretation prompts

```shell
python interpretation_prompts.py
```

Output: `interpretation/input/`

## 17. Submit interpretation prompts to GPT

```shell
python generate_interpretation_gpt.py \
    --input interpretation/input \
    --output interpretation/output \
    --model gpt-5.6-sol \
    --workers 4
```
Output: `interpretation/output/`

