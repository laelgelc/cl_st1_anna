# Perguntas

Oi, Rogerio. Bom dia!
Estou escrevendo o capítulo da metodologia, mas tem alguns pontos que eu não estou sabendo responder ou não estou achando nos arquivos. Pode me ajudar?

---

**Limitação do `gpt-6-luna` no denoising the alguns textos**

Revisando o seu projeto, notei que alguns textos provocaram o truncamento (corte) de texto pelo modelo `gpt-6-luna`. Detectei isso notando arquivos menores que 500 bytes na pasta `corpus/02_extracted`:

```shell
(my_env) eyamrog@eyamrog-Vivobook-16:~/PycharmProjects/cl_st1_anna/cl_st1_ph2_anna/corpus/02_extracted$ find . -type f -size -500c
./ms/ms_inf_e_ef_46.md
./es/es_ef_anos_finais_linguagens_ingles_1.md
./es/es_ef_anos_iniciais_linguagens_arte_1.md
./es/es_ef_anos_iniciais_ciencias_da_natureza_1.md
./se/se_inf_4.md
(my_env) eyamrog@eyamrog-Vivobook-16:~/PycharmProjects/cl_st1_anna/cl_st1_ph2_anna/corpus/02_extracted$
```

Por exemplo, o texto `es_ef_anos_finais_linguagens_ingles_1.md`, que corresponde ao `t000979` em `file_ids.txt`:

```text
t000979 es/es_ef_anos_finais_linguagens_ingles_1.txt
```

, resultou em:

Samba do Approach  
(Zeca Baleiro, 1999)

> “Venha provar meu brunch  
> Saiba que eu tenho approach  
> Na hora do lunch  
> Eu ando de ferryboat

quando, na realidade, o texto antes do denoising era maior: `cl_st1_ph2_anna/corpus/00_source_per_state/es/es_ef_anos_finais_linguagens_ingles_1.txt`

Assim sendo, houve perda de texto nestes 5 textos, causando um impacto desprezível na Análise Multidimensional Lexical.

Eu acredito que foi uma limitação tecnológica do modelo `gpt-6-luna` apesar deste ser um dos modelos mais recentes da OpenAI.

---

1. A tabela disponível na pasta interpretation > input indica quantos documentos por estado, mas a soma dos valores informados é 4.311 textos, enquanto selecionei 4.111. Qual está correto?

Resposta: O número correto é 4111, pois essa é a soma da coluna `N` da tabela a seguir, transcrita da pasta mencionada. O número 4311, aparentemente, não é mencionado em nenhum lugar dessa fase.

**Mean State Scores**

| Effect | State |   N |  Mean fac1 |    SD fac1 |
|--------|------:|----:|-----------:|-----------:|
| state  |    ac | 139 | 18.9352518 | 12.0915641 |
| state  |    al | 170 | 19.2882353 | 10.8831547 |
| state  |    am | 148 | 16.9527027 | 13.4722362 |
| state  |    ap | 134 | 19.2388060 | 12.3289372 |
| state  |    ba | 135 | 22.3555556 | 14.9394133 |
| state  |    ce | 148 | 25.0472973 | 15.8158340 |
| state  |    df | 103 | 20.9805825 | 12.6560693 |
| state  |    es | 104 | 17.8846154 | 13.2542777 |
| state  |    go | 150 | 22.4466667 | 13.9897070 |
| state  |    ma | 146 | 24.0479452 | 14.4862990 |
| state  |    mg | 293 | 16.7849829 |  9.2690851 |
| state  |    ms | 102 | 18.9117647 | 14.6848767 |
| state  |    mt | 227 | 23.3964758 | 15.1611283 |
| state  |    pa | 175 | 28.1828571 | 16.0032591 |
| state  |    pb | 209 | 20.4401914 | 14.2588539 |
| state  |    pe | 158 | 16.6835443 | 10.3807076 |
| state  |    pi | 127 | 24.4251969 | 14.7047772 |
| state  |    pr | 178 | 33.6966292 | 19.1776733 |
| state  |    rj |  98 | 14.6326531 |  9.8120353 |
| state  |    rn | 149 | 16.5704698 | 12.2161031 |
| state  |    ro | 279 | 20.8817204 | 14.9943751 |
| state  |    rr | 164 | 17.2926829 | 12.2384166 |
| state  |    rs | 141 | 17.7943262 | 12.2937369 |
| state  |    sc | 118 | 36.8305085 | 20.8500159 |
| state  |    se |  68 | 22.8088235 | 14.3758269 |
| state  |    sp | 103 | 22.2718447 | 10.5451356 |
| state  |    to | 145 | 16.5793103 | 13.1242296 |

Nota: Em decorrência da perda de texto no texto `t000979`, este acabou não tendo nenhuma contagem de variáveis no `cl_st1_ph2_anna/sas/counts.txt`. O script SAS (`cl_st1_ph2_anna/sas/cl_st1_ph2_anna.sas`), exclui textos nessas condições da análise estatística.

```text
t000979 es 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

Por isso, embora a quantidade de textos tenha sido 4112, como indica `cl_st1_ph2_anna/corpus_size/corpus_size.tsv` (transcrita a seguir), as tabelas de escore médio de fator indicam 4111.

|   Strata    | Text Count |  Word Count |
|:-----------:|-----------:|------------:|
|     ac      |        139 |      134414 |
|     al      |        170 |      146943 |
|     am      |        148 |      135457 |
|     ap      |        134 |      109215 |
|     ba      |        135 |      149420 |
|     ce      |        148 |      169600 |
|     df      |        103 |       90002 |
|     es      |        105 |       86277 |
|     go      |        150 |      168720 |
|     ma      |        146 |      155939 |
|     mg      |        293 |      206012 |
|     ms      |        102 |       84183 |
|     mt      |        227 |      236989 |
|     pa      |        175 |      214626 |
|     pb      |        209 |      180126 |
|     pe      |        158 |      106267 |
|     pi      |        127 |      127722 |
|     pr      |        178 |      254525 |
|     rj      |         98 |       73899 |
|     rn      |        149 |      112219 |
|     ro      |        279 |      251705 |
|     rr      |        164 |      128834 |
|     rs      |        141 |      107161 |
|     sc      |        118 |      206777 |
|     se      |         68 |       69510 |
|     sp      |        103 |       86262 |
|     to      |        145 |      120683 |
| **overall** |   **4112** | **3913487** |

2. Qual etiquetador linguístico foi utilizado e como ocorreu a lematização.

Resposta: O etiquetador foi o TreeTagger, que automaticamente realiza a lematização. Por exemplo, no extrato de texto etiquetado a sequir (`cl_st1_ph2_anna/corpus/07_tagged/es/es_ef_anos_finais_linguagens_ingles_1.txt`), a primeira coluna é a palavra (token), a segunda, é a etiqueta (tag), e a terceira é o lema (lemma).

```text
Samba	NOUN.Masc.Sing	samba
do	ADP_DET.Masc.Sing	de_o
Approach	NOUN.Masc.Sing	approach
```

3. Como os lemas-chave foram calculados e qual corpus ou distribuição serviu de referência.

Resposta: Os lemas-chave foram calculados comparando cada subcorpus em `cl_st1_ph2_anna/corpus/07_tagged` com os demais, como corpus de referência. Por exemplo, o subcorpus `ac` foi comparado com todos os demais, `al`, `am`, etc.. A comparação foi realizada através da estatística de comparação Log-likelihood (Scott, 1997). Refira-se ao programa `cl_st1_ph2_anna/keylemmas.py`.

Scott, M. (1997). PC analysis of key words—And key key words. System, 25(2), 233–245. https://doi.org/10.1016/S0346-251X(97)00011-0

4. Por que foram selecionadas até 45 palavras-chave por estado.

Resposta: Foram extraídas 45 palavras-chave por subcorpus (estado) para selecionar por volta de 1000 variáveis lexicais de forma estratificada. Essa seleção foi realizada através do programa `cl_st1_ph2_anna/select_kws_stratified.py` e resultou em 1037 variáveis.

```text
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

ac                     → selected 45/45 from 226 available POSKW lemmas
al                     → selected 45/45 from 75 available POSKW lemmas
am                     → selected 45/45 from 147 available POSKW lemmas
ap                     → selected 33/45 from 33 available POSKW lemmas
ba                     → selected 45/45 from 294 available POSKW lemmas
ce                     → selected 45/45 from 329 available POSKW lemmas
df                     → selected 45/45 from 93 available POSKW lemmas
es                     → selected 45/45 from 107 available POSKW lemmas
go                     → selected 45/45 from 324 available POSKW lemmas
ma                     → selected 45/45 from 215 available POSKW lemmas
mg                     → selected 22/45 from 22 available POSKW lemmas
ms                     → selected 45/45 from 122 available POSKW lemmas
mt                     → selected 45/45 from 215 available POSKW lemmas
pa                     → selected 45/45 from 605 available POSKW lemmas
pb                     → selected 45/45 from 116 available POSKW lemmas
pe                     → selected 45/45 from 52 available POSKW lemmas
pi                     → selected 45/45 from 157 available POSKW lemmas
pr                     → selected 45/45 from 781 available POSKW lemmas
rj                     → selected 45/45 from 106 available POSKW lemmas
rn                     → selected 45/45 from 64 available POSKW lemmas
ro                     → selected 45/45 from 102 available POSKW lemmas
rr                     → selected 45/45 from 53 available POSKW lemmas
rs                     → selected 45/45 from 76 available POSKW lemmas
sc                     → selected 45/45 from 1088 available POSKW lemmas
se                     → selected 45/45 from 130 available POSKW lemmas
sp                     → selected 45/45 from 91 available POSKW lemmas
to                     → selected 45/45 from 94 available POSKW lemmas

Total consolidated keywords before de-duplication: 1180
Unique keywords after de-duplication: 1037
Duplicates removed: 143

Final unique keywords written to: corpus/09_kw_selected/keywords.txt
Final unique keyword count: 1037
```

5. Como foram tratadas palavras funcionais, siglas, nomes próprios e possíveis ruídos de extração.

Resposta: As palavras-chave foram consideradas entre as etiquetadas como substantivos, verbos, e adjetivos. As demais foram excluídas. Refira-se ao programa `cl_st1_ph2_anna/keylemmas.py`.

```text
VALID_TAG_PREFIXES = (
    "NOUN",
#    "PROPN",
    "VERB",
    "ADJ",
#    "ADV",
)
```

6. Se as frequências foram normalizadas pela extensão dos textos antes da análise fatorial.

Resposta: As frequências levadas à análise fatorial foram binárias, sendo `1`, presença de variável, e `0`, ausência. Portanto, o conceito de normalização por extensão de texto não se aplica. Refira-se ao documento `cl_st1_ph2_anna/sas/counts.txt`.

```text
t000001 ac 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

7. O texto menciona simultaneamente colunas binárias e matriz de contagens. É necessário esclarecer se as variáveis foram operacionalizadas como presença/ausência ou como frequências, e se houve normalização por extensão textual.

Resposta: As variáveis foram operacionalizadas como presença/ausência.

8. Foram examinados exatamente 25 textos por polo nos quatro fatores? Caso algum polo tenha sido analisado com um número diferente de textos, a metodologia deverá registrar essa exceção.

Resposta: Para cada polo de fator, programa `cl_st1_ph2_anna/examples_txt.py` seleciona 20 exemplos do grupo (estado) de média mais alta e 10 dos demais grupos ordenados decrescentemente. Como há 26 grupos, o programa selecionou 20 + 10 x 26 = 280 exemplos. Você deve ter decidido selecionar 25 exemplos por polo por fator segundo um critério particular.

9. Informações que precisam ser preenchidas

| Informação                       | Detalhamento necessário                                                                                 | Resposta                                                                                                                                                                                                                                                                 |
|----------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Método de extração               | Se foi utilizado **Principal Components**, **Principal Factor**, **Maximum Likelihood** ou outro método | Principal Components                                                                                                                                                                                                                                                     |
| Método de rotação                | Se foi utilizada rotação **Varimax**, **Promax** ou outra                                               | Promax                                                                                                                                                                                                                                                                   |
| Critério das cargas fatoriais    | Se foi adotado um **limite numérico** ou uma **quantidade fixa de variáveis de maior carga por polo**   | Limite numérico de carga fatorial igual ou superior a 0,30                                                                                                                                                                                                               |
| Critérios adicionais de retenção | Se foram considerados **variância explicada**, **interpretabilidade dos fatores** ou outros indicadores | A retenção dos fatores baseou-se no critério de Kaiser (autovalores superiores a 1) e na inspeção visual do scree plot. O número final de fatores foi definido manualmente pelo pesquisador. Adicionalmente, foram removidas variáveis com comunalidade inferior a 0,15. |

10. ANOVA

Para finalizar esta subseção, será necessário consultar as saídas do SAS e verificar:

a) Nível de significância: se foi adotado α = 0,05.

Resposta: Foi adotado nível de significância de 5% (α = 0,05) para avaliar diferenças estatisticamente significativas entre os estados para os escores fatoriais das quatro dimensões.

b) Pressupostos da ANOVA: se foram realizados testes de normalidade dos resíduos e homogeneidade das variâncias.

Resposta: Não foram realizados.

c) Procedimento estatístico: se a ANOVA foi executada com PROC ANOVA, PROC GLM ou outro procedimento do SAS.

Resposta: Foi utilizado o procedimento PROC GLM (General Linear Model) do SAS.

d) Comparações múltiplas: se foram realizados testes posteriores à ANOVA.

Resposta: Não foram realizados nenhum teste posterior à ANOVA.

e) Dependência entre observações: se foi avaliado o agrupamento de seções dentro dos mesmos documentos curriculares.

Resposta: Essa dependência não foi avaliada.

f) A ANOVA convencional pressupõe independência das observações. Como seu corpus foi segmentado em seções, textos provenientes de um mesmo referencial curricular podem compartilhar características linguísticas em razão da autoria institucional e da organização documental. Isso significa que o número de textos não corresponde necessariamente ao número de observações estatisticamente independentes. Recomendo verificar como essa dependência foi tratada no SAS. Caso não tenha sido controlada, a tese deve reconhecer explicitamente essa limitação, pois ela pode afetar os erros-padrão e os valores de significância da ANOVA. Não é necessário ampliar o objetivo da pesquisa, mas é importante assegurar que as inferências estatísticas sejam compatíveis com a estrutura dos dados.

Resposta: As dependências mencionadas não foram tratadas no SAS.