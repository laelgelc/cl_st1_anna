## Me
How does this programme count the number of words? Does it count the number of lines per tagged file and consolidate the per-file counts? Just analyse the code.

## AI Assistant
The programme **does not simply count the number of lines per tagged file**.

It counts **valid token lines** in each tagged `.txt` file, then consolidates those counts by state/stratum and overall.

## How word counting works

The key function is:

```python
def count_tokens_in_tagged_file(path: Path) -> int:
```


For each tagged file, it:

1. Opens the file.
2. Reads it line by line.
3. Strips whitespace from each line.
4. Skips empty lines.
5. Splits the line into fields:
   - first by tab: `line.split("\t")`
   - if that gives fewer than 3 fields, falls back to whitespace splitting: `line.split()`
6. Skips the line if it still has fewer than 3 fields.
7. Takes the first three fields as:

```python
word, tag, _lemma = parts[:3]
```


8. Counts the line only if:

```python
is_countable_token(word, tag)
```


returns `True`.

## What counts as a word?

A token is counted only if:

```python
if not word:
    return False

if not word[0].isalpha():
    return False

if tag.startswith(("PUNCT", "SYM")):
    return False

return True
```


So a line counts as one word/token if:

- the token string is not empty;
- the first character of the token is alphabetic;
- the tag does **not** start with `PUNCT`;
- the tag does **not** start with `SYM`.

This means the programme excludes, for example:

- blank lines;
- malformed lines with fewer than three fields;
- punctuation tokens;
- symbol tokens;
- tokens beginning with a digit or non-letter character.

It includes tokens whose first character is alphabetic, including accented Unicode letters.

## Does it count lines per tagged file?

**Partly, but with filtering.**

Each valid tagged token line contributes `1` to the word count. So if a tagged file has one token per line, then the programme is effectively counting token lines — **but only token lines that pass the filters above**.

It is **not** counting all lines blindly.

For example, these would count:

```plain text
educação	NOUN	educação
brasileira	ADJ	brasileiro
```


These would not count:

```plain text
,	PUNCT	,
2024	NUM	2024
%	SYM	%
```


## How the counts are consolidated

The programme processes files under:

```python
CORPUS_ROOT = Path("corpus/07_tagged")
```


It expects state/stratum folders such as:

```plain text
corpus/07_tagged/ac/
corpus/07_tagged/es/
corpus/07_tagged/sp/
```


Only folders whose names match two lowercase letters are treated as strata:

```python
STATE_PATTERN = re.compile(r"^[a-z]{2}$")
```


For each state folder, it gets only direct `.txt` files:

```python
text_files = sorted(
    strata_dir.glob("*.txt"),
    key=lambda path: natural_sort_key(path.name),
)
```


Then for each file:

```python
words = count_tokens_in_tagged_file(text_file)

file_counts_strata[strata] += 1
word_counts_strata[strata] += words

total_files += 1
total_words += words
```


So yes: it performs a **per-file count**, adds that count to the relevant state/stratum total, and also adds it to the overall total.

## Output

It writes a TSV file here:

```python
OUTPUT_FILE = OUTPUT_DIR / "corpus_size.tsv"
```


with columns:

```plain text
Strata	Text Count	Word Count
```


For each stratum, it writes:

```python
f"{strata}\t"
f"{file_counts_strata[strata]}\t"
f"{word_counts_strata[strata]}\n"
```


Then it writes an overall line:

```python
f"overall\t{total_files}\t{total_words}\n"
```


## Summary

Yes, the programme:

1. finds tagged `.txt` files inside each two-letter state folder;
2. counts words per file;
3. consolidates those counts by state/stratum;
4. calculates overall totals.

But importantly, the “word count” is **not just the number of lines**. It is the number of **valid tagged token lines**, excluding punctuation, symbols, malformed lines, blank lines, and tokens whose first character is not alphabetic.

## Me
Please adapt the `corpus_size.py` programme (attached) include the `Stage` column to the right of the `Strata` column. `Stage` should be captured from each input filename. For example:

```plain text
Example:
    corpus/07_tagged/ac/ac_ef_1.txt -> Stage = ef
    corpus/07_tagged/go/go_em_1.txt -> Stage = em
    corpus/07_tagged/se/se_inf_1.txt -> Stage = inf
```


The possible values are:

{'inf',
 'inf_e_ef',
 'inf_ef',
 'ef',
 'ef_e_em',
 'em'}

For each state (`Strata` column), the `Stage` column should be presented in the order of the list, except when the state does not have any documents in one of the categories.

`Text Count` and `Word Count` should be grouped by `Stage` accordingly.

Create the option `--ample` where the possible values are shown below. In this case, the output file should be named `corpus_size/corpus_size_ample.tsv`.

{'inf',
 'inf_10_camp_exp',
 'inf_12_camp_exp_escuta_fala',
 'inf_1_concepces',
 'inf_2_principios',
 'inf_3_direitos',
 'inf_4_planejamento',
 'inf_5_acolhimento',
 'inf_8_camp_exp',
 'inf_adaptacoes',
 'inf_agrupamentos',
 'inf_alfabetizar',
 'inf_apresentacao',
 'inf_aspectos_pedagogicos',
 'inf_avaliacao',
 'inf_cam_exp',
 'inf_camp_ex',
 'inf_camp_exp',
 'inf_campo_e_indigena',
 'inf_campo_exp',
 'inf_concepcao_de_infancia',
 'inf_curriculo',
 'inf_curriculo_e_ppp',
 'inf_direitos_de_aprendizagem',
 'inf_diversidade_etnico_racial',
 'inf_e_ef',
 'inf_e_ef_apresentacao',
 'inf_e_ef_intro',
 'inf_ef',
 'inf_espacos',
 'inf_final',
 'inf_finalidade',
 'inf_formacao_de_professores',
 'inf_formacao_leitora',
 'inf_funcao_social',
 'inf_inclusao',
 'inf_intro',
 'inf_intro_14_matriz_saberes',
 'inf_intro_16_temas_integradores',
 'inf_intro_19_dinamicas',
 'inf_intro_20_avaliacao',
 'inf_ludico',
 'inf_natureza',
 'inf_objetivos',
 'inf_organizacao',
 'inf_papel_do_professor',
 'inf_planejamento',
 'inf_principios',
 'inf_provinha',
 'inf_respeito_e_diversidade',
 'inf_trajetoria',
 'inf_transicoes',
 'ef',
 'ef_anos_finais_ciencias_da_natureza',
 'ef_anos_finais_linguagens_ingles',
 'ef_anos_iniciais_arte',
 'ef_anos_iniciais_ciencias_da_natureza',
 'ef_anos_iniciais_ciencias_humanas_geo',
 'ef_anos_iniciais_ciencias_humanas_historia',
 'ef_anos_iniciais_ciencias_humanas_intro',
 'ef_anos_iniciais_ensino_religioso',
 'ef_anos_iniciais_linguagens_arte',
 'ef_anos_iniciais_linguagens_ed_fis',
 'ef_anos_iniciais_linguagens_intro',
 'ef_anos_iniciais_linguagens_lp',
 'ef_anos_iniciais_matematica',
 'ef_ch_geo',
 'ef_ch_his',
 'ef_ciencias',
 'ef_ciencias_da_natureza',
 'ef_ciencias_da_natureza_intro',
 'ef_ciencias_humanas_geo',
 'ef_ciencias_humanas_his',
 'ef_ciencias_humanas_intro',
 'ef_ciencias_humas_intro',
 'ef_e_em_tema_integrador',
 'ef_ensino_religioso',
 'ef_er',
 'ef_intro',
 'ef_linguagens_arte',
 'ef_linguagens_ed_fis',
 'ef_linguagens_ingles',
 'ef_linguagens_intro',
 'ef_linguagens_lp',
 'ef_matematica',
 'ef_matematica_intro',
 'em'}

Is it clear?

## AI Assistant
Yes, it is clear.

Below is an adapted version of `corpus_size.py` that:

- adds a `Stage` column immediately after `Strata`;
- extracts `Stage` from each filename;
- groups `Text Count` and `Word Count` by `(Strata, Stage)`;
- preserves the requested stage order;
- adds `--ample`;
- writes:
  - default output to `corpus_size/corpus_size.tsv`;
  - `--ample` output to `corpus_size/corpus_size_ample.tsv`.
