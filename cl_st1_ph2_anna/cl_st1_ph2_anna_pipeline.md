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
