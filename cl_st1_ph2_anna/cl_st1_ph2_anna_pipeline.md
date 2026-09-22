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
    --model gpt-5.6-luna \
    --limit 10 \
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
    --prompt denoising_prompts/denoising_v1.md \
    --model gpt-5.6-luna \
    --limit 200 \
    --workers 10 \
    --resume \
    --max-output-tokens 1000
```

### Full run

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v1.md \
    --model gpt-5.6-luna \
    --workers 10 \
    --resume \
    --max-output-tokens 1000 \
    --max-retries 5
```

### Production mode on an EC2 instance

```shell
bash run_python_ec2.sh \
    llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/02_extracted \
    --prompt denoising_prompts/denoising_v1.md \
    --model gpt-5.6-luna \
    --workers 10 \
    --resume \
    --max-output-tokens 1000 \
    --max-retries 5
```
