# Corpus Linguistics - Study 1 - Phase 2 - Anna

Run the commands from the project phase directory, e.g.:

```text
cl_st1_ph2_anna/
```

## 1. Denoise the texts

### Dry run

```shell
python llm_denoise.py \
    --manifest corpus/brazilian_educational_guidelines.ndjson \
    --output corpus/03_now_screened/llm_screening_v2_gpt-5.6-luna \
    --prompt llm_screening_prompts/llm_screening_v2.md \
    --model gpt-5.6-luna \
    --limit 10 \
    --dry-run
```


### Test run, first time

```shell
python llm_screening.py \
    --manifest corpus/palestine_now.ndjson \
    --output corpus/03_now_screened/llm_screening_v2_gpt-5.6-luna \
    --prompt llm_screening_prompts/llm_screening_v2.md \
    --model gpt-5.6-luna \
    --limit 10
```

### 20 workers test run

```shell
python llm_screening.py \
    --manifest corpus/palestine_now.ndjson \
    --output corpus/03_now_screened/llm_screening_v2_gpt-5.6-luna \
    --prompt llm_screening_prompts/llm_screening_v2.md \
    --model gpt-5.6-luna \
    --limit 200 \
    --workers 20 \
    --resume \
    --max-output-tokens 1000
```

### Full run

```shell
python llm_screening.py \
    --manifest corpus/palestine_now.ndjson \
    --output corpus/03_now_screened/llm_screening_v2_gpt-5.6-luna \
    --prompt llm_screening_prompts/llm_screening_v2.md \
    --model gpt-5.6-luna \
    --workers 20 \
    --resume \
    --max-output-tokens 1000 \
    --max-retries 5
```

### Production mode on an EC2 instance

```shell
bash run_python_ec2.sh \
    llm_screening.py \
    --manifest corpus/palestine_now.ndjson \
    --output corpus/03_now_screened/llm_screening_v2_gpt-5.6-luna \
    --prompt llm_screening_prompts/llm_screening_v2.md \
    --model gpt-5.6-luna \
    --workers 20 \
    --resume \
    --max-output-tokens 1000 \
    --max-retries 5
```