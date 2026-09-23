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

The programme was adapted to remove Markdown marker characters that should not be tagged as tokens.

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

Output: `corpus/08_keylemmas/<group>.tsv`

## 4. Select a stratified keyword set

```shell
python select_kws_stratified.py \
    --input corpus/08_keylemmas \
    --output corpus/09_kw_selected \
    --per-group 45 \
    --max-total 20000
```

Output: `corpus/09_kw_selected/keywords.txt

```shell
=== Stratum Keyword Quotas ===
ac                     → 45 keywords max
al                     → 45 keywords max
am                     → 45 keywords max
ap                     → 45 keywords max
ba                     → 45 keywords max
ce                     → 45 keywords max
df                     → 45 keywords max
es                     → 45 keywords max
go                     → 45 keywords max
ma                     → 45 keywords max
mg                     → 45 keywords max
ms                     → 45 keywords max
mt                     → 45 keywords max
pa                     → 45 keywords max
pb                     → 45 keywords max
pe                     → 45 keywords max
pi                     → 45 keywords max
pr                     → 45 keywords max
rj                     → 45 keywords max
rn                     → 45 keywords max
ro                     → 45 keywords max
rr                     → 45 keywords max
rs                     → 45 keywords max
sc                     → 45 keywords max
se                     → 45 keywords max
sp                     → 45 keywords max
to                     → 45 keywords max
==============================

ac                     → selected 45/45 from 246 available POSKW lemmas
al                     → selected 45/45 from 89 available POSKW lemmas
am                     → selected 45/45 from 170 available POSKW lemmas
ap                     → selected 45/45 from 46 available POSKW lemmas
ba                     → selected 45/45 from 356 available POSKW lemmas
ce                     → selected 45/45 from 368 available POSKW lemmas
df                     → selected 45/45 from 120 available POSKW lemmas
es                     → selected 45/45 from 124 available POSKW lemmas
go                     → selected 45/45 from 364 available POSKW lemmas
ma                     → selected 45/45 from 244 available POSKW lemmas
mg                     → selected 30/45 from 30 available POSKW lemmas
ms                     → selected 45/45 from 147 available POSKW lemmas
mt                     → selected 45/45 from 252 available POSKW lemmas
pa                     → selected 45/45 from 679 available POSKW lemmas
pb                     → selected 45/45 from 140 available POSKW lemmas
pe                     → selected 45/45 from 68 available POSKW lemmas
pi                     → selected 45/45 from 191 available POSKW lemmas
pr                     → selected 45/45 from 853 available POSKW lemmas
rj                     → selected 45/45 from 121 available POSKW lemmas
rn                     → selected 45/45 from 74 available POSKW lemmas
ro                     → selected 45/45 from 110 available POSKW lemmas
rr                     → selected 45/45 from 65 available POSKW lemmas
rs                     → selected 45/45 from 92 available POSKW lemmas
sc                     → selected 45/45 from 1150 available POSKW lemmas
se                     → selected 45/45 from 161 available POSKW lemmas
sp                     → selected 45/45 from 98 available POSKW lemmas
to                     → selected 45/45 from 102 available POSKW lemmas

Total consolidated keywords before de-duplication: 1200
Unique keywords after de-duplication: 1063
Duplicates removed: 137

Final unique keywords written to: corpus/09_kw_selected/keywords.txt
Final unique keyword count: 1063
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

