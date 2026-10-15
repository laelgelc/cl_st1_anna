## Perguntas

[14/10/26, 09:14:09] ~Anna Freire: Oi, Rogério. Bom dia! A Claudia leu meu texto e fez umas perguntas metodológicas que eu não sei responder. Pode me ajudar?

### Pergunta 1

[14/10/26, 09:14:16] ~Anna Freire:

> ## A ANOVA: diferenças entre estados e estrutura dos dados
> 
> Os resultados indicam diferenças estatisticamente significativas entre os estados nos quatro fatores. O primeiro apresenta a maior proporção de variância associada ao estado. Entretanto, a interpretação estatística exige uma questão adicional:
>
> A tese reconhece que a quantidade de textos varia entre estados, mas essa é uma questão distinta da dependência entre observações.
>
> **Qual é a relação entre o número de unidades textuais por estado e a precisão das estimativas?**
>
> Precisa explicar se as diferenças encontradas representam diferenças entre as médias dos escores fatoriais dos grupos, ou se permitem caracterizar diretamente diferenças nas políticas curriculares estaduais

Resposta (assistida pelo AI Assistant):

A variação no número de unidades textuais por estado afeta principalmente a **precisão das estimativas das médias estaduais**. Estados com maior número de textos tendem a produzir estimativas mais estáveis dos escores fatoriais médios, pois a média é calculada com base em um conjunto mais amplo de observações. Em contrapartida, estados com menor número de textos apresentam estimativas mais sensíveis à composição específica do subcorpus, isto é, a presença ou ausência de poucos textos pode alterar mais fortemente a média estadual.

Essa questão, contudo, deve ser distinguida da dependência entre observações. A diferença no tamanho dos grupos diz respeito ao **peso e à precisão estatística** das estimativas; já a dependência entre observações diz respeito ao fato de que textos pertencentes a um mesmo estado podem compartilhar características comuns, pois derivam de um mesmo contexto institucional, normativo e curricular. Assim, as unidades textuais não devem ser interpretadas como observações plenamente independentes no sentido substantivo, ainda que tenham sido tratadas como unidades de análise na estimação dos escores fatoriais.

A ANOVA, nesse caso, testa se há diferenças estatisticamente significativas entre as **médias dos escores fatoriais dos grupos estaduais**. Portanto, os resultados permitem afirmar que os textos associados a determinados estados apresentam, em média, escores fatoriais distintos nos fatores analisados. Essa é uma evidência de diferenciação lexical e discursiva entre os subcorpora estaduais.

Entretanto, é necessário evitar uma inferência direta e automática entre diferenças nas médias dos escores fatoriais e diferenças substantivas nas políticas curriculares estaduais. Os fatores resultam de padrões de coocorrência lexical observados nos textos; por isso, eles permitem caracterizar diferenças na **manifestação textual** das políticas curriculares, e não necessariamente diferenças integrais nas políticas como objetos institucionais complexos. A interpretação substantiva das diferenças entre estados depende da articulação entre os resultados estatísticos, a composição do corpus, a leitura qualitativa dos termos associados a cada fator e o conhecimento contextual sobre os documentos curriculares.

Assim, a formulação mais adequada é dizer que a ANOVA identifica diferenças entre estados nas médias dos escores fatoriais dos textos. Essas diferenças sugerem contrastes relevantes na ênfase lexical e discursiva dos documentos curriculares estaduais, mas devem ser interpretadas como indicadores textuais das políticas, e não como uma caracterização direta e completa das políticas curriculares em si.

### Pergunta 2

[14/10/26, 09:14:21] ~Anna Freire:

> ## A seleção das variáveis lexicais
>
> A metodologia informa que foram identificadas 1.180 palavras-chave candidatas e, após a eliminação de duplicatas, mantidos 1.037 itens lexicais únicos. A seleção foi estratificada por estado, com limite de 45 palavras-chave por subcorpus estadual. A matriz foi construída com indicadores binários de presença e ausência dos lemas em cada texto.
>
> A opção tem uma justificativa compreensível: ampliar a representação lexical dos diferentes estados. No entanto, precisa explicar melhor como essa estratégia afeta a interpretação estatística. Deve-se discutir se a seleção favorece itens associados a contextos estaduais específicos, em detrimento de palavras recorrentes no conjunto do corpus.
>
> **Quais critérios foram utilizados para determinar que uma variável lexical seria mantida ou excluída da solução fatorial?**

Resposta (assistida pelo AI Assistant):

A seleção das variáveis lexicais foi realizada em duas etapas principais. Primeiro, foram identificadas palavras-chave candidatas em cada subcorpus estadual. Em seguida, essas listas foram consolidadas, duplicatas foram eliminadas e foi construída uma lista final de lemas a serem transformados em variáveis binárias de presença/ausência nos textos.

O critério inicial de inclusão foi, portanto, a **relevância lexical dentro de cada subcorpus estadual**. A seleção foi estratificada por estado, com limite aproximado de 45 palavras-chave por subcorpus, para evitar que estados com maior número de textos ou maior volume lexical dominassem a composição da matriz. Essa decisão buscou ampliar a representação dos diferentes contextos estaduais na etapa exploratória da análise fatorial.

Além disso, o número aproximado de variáveis lexicais foi definido com base em uma regra prática indicada por Biber para análises multidimensionais, segundo a qual é recomendável haver pelo menos cerca de **cinco textos por variável**. Como o corpus continha **4.112 textos**, essa razão indicaria aproximadamente:

4112 / 5 = 822,4

Assim, buscou-se uma solução em torno de mil variáveis lexicais, mantendo uma proporção considerada aceitável entre o número de observações e o número de variáveis. Após a seleção das palavras-chave candidatas e a eliminação de duplicatas, permaneceram **1.037 itens lexicais únicos**, número próximo ao alvo metodológico estabelecido.

Foram mantidas, portanto, as variáveis lexicais que atendiam simultaneamente a três condições:  
1. apareciam como palavras-chave em pelo menos um dos subcorpora estaduais;  
2. não eram duplicatas de lemas já selecionados;  
3. contribuíam para compor uma matriz lexical de tamanho compatível com o número total de textos disponíveis.

As variáveis foram excluídas quando eram duplicatas, quando não entravam no limite de seleção estabelecido para o respectivo subcorpus estadual ou quando não integravam a lista final consolidada de palavras-chave. Desse modo, a exclusão não decorreu de uma avaliação substantiva isolada de cada palavra, mas de critérios operacionais ligados à seleção estratificada, à não redundância lexical e à adequação da razão entre número de textos e número de variáveis.

Essa estratégia tem consequências para a interpretação estatística. Como a seleção foi estratificada por estado, ela tende a favorecer uma representação mais equilibrada dos diferentes subcorpora, inclusive de itens lexicais mais característicos de contextos estaduais específicos. Portanto, a matriz não deve ser interpretada como uma simples lista das palavras mais frequentes ou mais recorrentes no corpus total. Ela foi construída para captar tanto padrões lexicais amplos quanto marcas lexicais distintivas dos estados.

Por essa razão, a solução fatorial deve ser interpretada como uma análise dos padrões de associação entre os lemas selecionados, considerando uma amostra lexical deliberadamente balanceada por estado. Isso significa que os fatores não representam apenas os temas lexicalmente mais frequentes no conjunto do corpus, mas dimensões de variação produzidas a partir de um vocabulário selecionado para preservar a diversidade estadual. Essa opção fortalece a comparação entre estados, mas exige cautela: os fatores devem ser entendidos como dimensões lexicais emergentes dessa estratégia de seleção, e não como uma descrição exaustiva de todo o vocabulário recorrente nos documentos curriculares.

### Pergunta 3

> ## A retenção de quatro fatores: decisão estatística ou interpretativa?
>
> **Qual foi a proporção de variância explicada pela solução de quatro fatores e por cada fator individualmente?**

Resposta (assistida pelo AI Assistant):

A solução de quatro fatores explicou, em conjunto, aproximadamente **32,02% da variância** das variáveis lexicais retidas na análise fatorial. A distribuição da variância explicada por fator foi a seguinte:

|     Fator | Variância explicada |
|----------:|--------------------:|
|   Fator 1 |          **10,04%** |
|   Fator 2 |           **8,25%** |
|   Fator 3 |           **7,92%** |
|   Fator 4 |           **5,80%** |
| **Total** |          **32,02%** |

Esses percentuais foram calculados a partir da soma dos quadrados das cargas fatoriais da solução rotacionada, considerando as **1.003 variáveis lexicais retidas** após a exclusão das variáveis com baixa comunalidade. O cálculo desses resultados está em `cl_st1_ph2_anna.ipynb`.

A retenção dos quatro fatores não foi exclusivamente automática. Ela combinou critérios estatísticos e interpretativos: inicialmente, foram considerados o **critério de Kaiser**, isto é, autovalores superiores a 1, e a **inspeção visual do scree plot**. Além disso, variáveis com comunalidade inferior a **0,15** foram removidas. Após essa etapa, a solução de quatro fatores foi mantida por decisão do pesquisador, considerando também a **interpretabilidade substantiva** das dimensões resultantes.

Assim, a resposta metodológica pode ser formulada da seguinte maneira:

> A solução final de quatro fatores explicou 32,02% da variância total das 1.003 variáveis lexicais retidas na análise. Individualmente, o Fator 1 explicou 10,04% da variância, o Fator 2 explicou 8,25%, o Fator 3 explicou 7,92% e o Fator 4 explicou 5,80%. A retenção dos quatro fatores resultou da combinação entre critérios estatísticos — critério de Kaiser, inspeção visual do scree plot e exclusão de variáveis com comunalidade inferior a 0,15 — e avaliação interpretativa da solução pelo pesquisador.

### Pergunta 4

[14/10/26, 09:17:25] ~Anna Freire:

> Precisa apresentar uma caracterização quantitativa clara do corpus: número de documentos, unidades textuais, palavras e distribuição por estado e etapa de ensino. Essa caracterização permitiria ao leitor avaliar melhor o alcance dos resultados.

[14/10/26, 09:17:25] ~Anna Freire: Coloquei uma tabela com o número de textos por estado, mas não está suficiente. Eu acho essas informações que ela está pedindo na pasta?

Resposta: Esse nível de detalhe não estava previsto pelo programa `corpus_size.py`. Portanto, adaptei-o para gerar duas versões de tabela com o número de textos por estado e etapa de ensino. Escolha a que você achar melhor.

Esta é mais resumida:

> corpus_size/corpus_size.tsv

| Strata  | Stage        | Text Count | Word Count |
|---------|--------------|-----------:|-----------:|
| ac      | inf          |         26 |      35800 |
| ac      | inf_e_ef     |         12 |       7682 |
| ac      | ef           |         46 |      42945 |
| ac      | em           |         55 |      47987 |
| al      | inf          |         23 |      19917 |
| al      | ef           |        101 |      75084 |
| al      | em           |         46 |      51942 |
| am      | inf          |         49 |      43107 |
| am      | ef           |         57 |      56652 |
| am      | em           |         42 |      35698 |
| ap      | inf          |         17 |      10170 |
| ap      | inf_e_ef     |         13 |      14156 |
| ap      | ef           |         44 |      39261 |
| ap      | em           |         60 |      45628 |
| ba      | inf          |         11 |      10585 |
| ba      | inf_e_ef     |         25 |      28612 |
| ba      | ef           |         31 |      32950 |
| ba      | em           |         68 |      77273 |
| ce      | inf          |         17 |      22525 |
| ce      | inf_e_ef     |         31 |      38270 |
| ce      | ef           |         36 |      33001 |
| ce      | em           |         64 |      75804 |
| df      | inf          |         26 |      18680 |
| df      | ef           |         20 |      25673 |
| df      | em           |         57 |      45649 |
| es      | inf          |         41 |      28439 |
| es      | ef           |         36 |      25730 |
| es      | ef_e_em      |          1 |       3320 |
| es      | em           |         27 |      28788 |
| go      | inf          |         29 |      43972 |
| go      | inf_e_ef     |          7 |       7345 |
| go      | ef           |         47 |      43079 |
| go      | em           |         67 |      74324 |
| ma      | inf          |          9 |       8849 |
| ma      | inf_e_ef     |         16 |      17579 |
| ma      | ef           |         62 |      57608 |
| ma      | em           |         59 |      71903 |
| mg      | inf          |         29 |      16699 |
| mg      | inf_e_ef     |          7 |       6562 |
| mg      | ef           |        106 |      67916 |
| mg      | em           |        151 |     114835 |
| ms      | inf_e_ef     |         47 |      35463 |
| ms      | em           |         55 |      48720 |
| mt      | inf          |         25 |      20708 |
| mt      | ef           |        101 |      94516 |
| mt      | em           |         77 |      81647 |
| mt      | unclassified |         24 |      40118 |
| pa      | inf          |         19 |      19767 |
| pa      | inf_e_ef     |          5 |       4591 |
| pa      | ef           |         29 |      32248 |
| pa      | em           |        122 |     158020 |
| pb      | inf          |         28 |      15084 |
| pb      | inf_e_ef     |          5 |       3174 |
| pb      | ef           |         56 |      51381 |
| pb      | em           |        120 |     110487 |
| pe      | inf          |         29 |      18206 |
| pe      | ef           |         79 |      53677 |
| pe      | em           |         50 |      34384 |
| pi      | inf          |          7 |       5896 |
| pi      | inf_e_ef     |         17 |      10967 |
| pi      | ef           |         42 |      30054 |
| pi      | em           |         61 |      80805 |
| pr      | inf          |          8 |       7666 |
| pr      | inf_ef       |         17 |      13784 |
| pr      | ef           |         12 |      32063 |
| pr      | em           |        141 |     201012 |
| rj      | inf          |         43 |      27322 |
| rj      | inf_e_ef     |         11 |       7981 |
| rj      | ef           |         31 |      30269 |
| rj      | em           |         13 |       8327 |
| rn      | inf          |         41 |      31488 |
| rn      | ef           |         61 |      39892 |
| rn      | em           |         47 |      40839 |
| ro      | inf          |         53 |      29869 |
| ro      | ef           |        110 |      85848 |
| ro      | em           |        116 |     135988 |
| rr      | inf          |         26 |      13140 |
| rr      | inf_e_ef     |          5 |       3832 |
| rr      | ef           |         67 |      55794 |
| rr      | em           |         66 |      56068 |
| rs      | inf          |         19 |      13799 |
| rs      | inf_e_ef     |         19 |       9654 |
| rs      | ef           |         12 |       9995 |
| rs      | em           |         91 |      73713 |
| sc      | inf_e_ef     |         38 |      53801 |
| sc      | em           |         80 |     152976 |
| se      | inf          |          9 |       8858 |
| se      | inf_e_ef     |          3 |       5201 |
| se      | ef           |         24 |      18676 |
| se      | em           |         32 |      36775 |
| sp      | inf          |         10 |       5782 |
| sp      | inf_e_ef     |         11 |       6824 |
| sp      | ef           |         37 |      35054 |
| sp      | em           |         45 |      38602 |
| to      | inf          |         31 |      22043 |
| to      | ef           |         39 |      40692 |
| to      | em           |         75 |      57948 |
|         |              |            |            |
| overall | inf          |        625 |     498371 |
| overall | inf_e_ef     |        272 |     261694 |
| overall | inf_ef       |         17 |      13784 |
| overall | ef           |       1286 |    1110058 |
| overall | ef_e_em      |          1 |       3320 |
| overall | em           |       1887 |    1986142 |
| overall | unclassified |         24 |      40118 |
|         |              |            |            |
| overall | overall      |       4112 |    3913487 |

Legenda:

- inf: ensino infantil
- inf_e_ef: ensino infantil e ensino fundamental
- inf_ef: ensino infantil e ensino fundamental
- ef: ensino fundamental
- ef_e_em: ensino fundamental e ensino médio
- em: ensino médio

Esta é mais ampla:

> corpus_size/corpus_size_ample.tsv

| Strata  | Stage                                      | Text Count | Word Count |
|---------|--------------------------------------------|-----------:|-----------:|
| ac      | inf                                        |         26 |      35800 |
| ac      | inf_e_ef                                   |         12 |       7682 |
| ac      | ef                                         |         46 |      42945 |
| ac      | em                                         |         55 |      47987 |
| al      | inf                                        |         23 |      19917 |
| al      | ef                                         |        101 |      75084 |
| al      | em                                         |         46 |      51942 |
| am      | inf                                        |         49 |      43107 |
| am      | ef                                         |         57 |      56652 |
| am      | em                                         |         42 |      35698 |
| ap      | inf                                        |         17 |      10170 |
| ap      | inf_e_ef                                   |         13 |      14156 |
| ap      | ef                                         |         44 |      39261 |
| ap      | em                                         |         60 |      45628 |
| ba      | inf                                        |         11 |      10585 |
| ba      | inf_e_ef                                   |         25 |      28612 |
| ba      | ef                                         |         31 |      32950 |
| ba      | em                                         |         68 |      77273 |
| ce      | inf                                        |         17 |      22525 |
| ce      | inf_e_ef                                   |         31 |      38270 |
| ce      | ef                                         |         36 |      33001 |
| ce      | em                                         |         64 |      75804 |
| df      | inf                                        |         26 |      18680 |
| df      | ef                                         |         20 |      25673 |
| df      | em                                         |         57 |      45649 |
| es      | inf                                        |         10 |       5361 |
| es      | inf_10_camp_exp                            |          1 |        752 |
| es      | inf_12_camp_exp_escuta_fala                |          1 |        660 |
| es      | inf_1_concepces                            |          1 |        537 |
| es      | inf_2_principios                           |          1 |        464 |
| es      | inf_3_direitos                             |          1 |        449 |
| es      | inf_4_planejamento                         |          1 |        662 |
| es      | inf_5_acolhimento                          |          1 |       1055 |
| es      | inf_8_camp_exp                             |          1 |        738 |
| es      | inf_apresentacao                           |          1 |        880 |
| es      | inf_intro                                  |         18 |      14041 |
| es      | inf_intro_14_matriz_saberes                |          1 |        555 |
| es      | inf_intro_16_temas_integradores            |          1 |       1323 |
| es      | inf_intro_19_dinamicas                     |          1 |        408 |
| es      | inf_intro_20_avaliacao                     |          1 |        554 |
| es      | ef_anos_finais_ciencias_da_natureza        |          1 |        251 |
| es      | ef_anos_finais_linguagens_ingles           |          2 |       1117 |
| es      | ef_anos_iniciais_arte                      |          4 |       2441 |
| es      | ef_anos_iniciais_ciencias_da_natureza      |          4 |       3039 |
| es      | ef_anos_iniciais_ciencias_humanas_geo      |          2 |       2043 |
| es      | ef_anos_iniciais_ciencias_humanas_historia |          2 |       1850 |
| es      | ef_anos_iniciais_ciencias_humanas_intro    |          1 |        678 |
| es      | ef_anos_iniciais_ensino_religioso          |          2 |       1514 |
| es      | ef_anos_iniciais_linguagens_arte           |          1 |         35 |
| es      | ef_anos_iniciais_linguagens_ed_fis         |          2 |       1240 |
| es      | ef_anos_iniciais_linguagens_intro          |          4 |       2474 |
| es      | ef_anos_iniciais_linguagens_lp             |          7 |       5100 |
| es      | ef_anos_iniciais_matematica                |          3 |       3227 |
| es      | ef_e_em_tema_integrador                    |          1 |       3320 |
| es      | ef_intro                                   |          1 |        721 |
| es      | em                                         |         27 |      28788 |
| go      | inf                                        |         29 |      43972 |
| go      | inf_e_ef                                   |          7 |       7345 |
| go      | ef                                         |         47 |      43079 |
| go      | em                                         |         67 |      74324 |
| ma      | inf                                        |          9 |       8849 |
| ma      | inf_e_ef                                   |         16 |      17579 |
| ma      | ef                                         |         62 |      57608 |
| ma      | em                                         |         59 |      71903 |
| mg      | inf_adaptacoes                             |          2 |        995 |
| mg      | inf_avaliacao                              |          1 |        948 |
| mg      | inf_camp_exp                               |          3 |       3003 |
| mg      | inf_campo_exp                              |          3 |       1869 |
| mg      | inf_e_ef_intro                             |          7 |       6562 |
| mg      | inf_final                                  |          1 |        372 |
| mg      | inf_inclusao                               |          7 |       3220 |
| mg      | inf_intro                                  |          1 |        501 |
| mg      | inf_objetivos                              |          1 |        547 |
| mg      | inf_organizacao                            |          2 |        709 |
| mg      | inf_planejamento                           |          2 |       1362 |
| mg      | inf_principios                             |          5 |       2554 |
| mg      | inf_trajetoria                             |          1 |        619 |
| mg      | ef_ch_geo                                  |         11 |       6943 |
| mg      | ef_ch_his                                  |          7 |       4734 |
| mg      | ef_ciencias                                |          9 |       5329 |
| mg      | ef_ciencias_da_natureza_intro              |          1 |        654 |
| mg      | ef_ciencias_humanas_intro                  |          3 |       1490 |
| mg      | ef_ciencias_humas_intro                    |          1 |        622 |
| mg      | ef_er                                      |         10 |       5682 |
| mg      | ef_intro                                   |          3 |       3104 |
| mg      | ef_linguagens_arte                         |          9 |       5305 |
| mg      | ef_linguagens_ed_fis                       |         13 |       7590 |
| mg      | ef_linguagens_ingles                       |         14 |       7207 |
| mg      | ef_linguagens_intro                        |          1 |        995 |
| mg      | ef_linguagens_lp                           |         17 |      13036 |
| mg      | ef_matematica                              |          6 |       4524 |
| mg      | ef_matematica_intro                        |          1 |        701 |
| mg      | em                                         |        151 |     114835 |
| ms      | inf_e_ef                                   |         47 |      35463 |
| ms      | em                                         |         55 |      48720 |
| mt      | inf                                        |         25 |      20708 |
| mt      | ef                                         |        101 |      94516 |
| mt      | em                                         |         77 |      81647 |
| mt      | unclassified                               |         24 |      40118 |
| pa      | inf                                        |         19 |      19767 |
| pa      | inf_e_ef                                   |          5 |       4591 |
| pa      | ef                                         |         29 |      32248 |
| pa      | em                                         |        122 |     158020 |
| pb      | inf                                        |         28 |      15084 |
| pb      | inf_e_ef                                   |          5 |       3174 |
| pb      | ef                                         |         56 |      51381 |
| pb      | em                                         |        120 |     110487 |
| pe      | inf                                        |         29 |      18206 |
| pe      | ef                                         |         79 |      53677 |
| pe      | em                                         |         50 |      34384 |
| pi      | inf                                        |          7 |       5896 |
| pi      | inf_e_ef                                   |         17 |      10967 |
| pi      | ef                                         |         42 |      30054 |
| pi      | em                                         |         61 |      80805 |
| pr      | inf                                        |          8 |       7666 |
| pr      | inf_ef                                     |         17 |      13784 |
| pr      | ef                                         |         12 |      32063 |
| pr      | em                                         |        141 |     201012 |
| rj      | inf_alfabetizar                            |          3 |       1642 |
| rj      | inf_cam_exp                                |          7 |       4852 |
| rj      | inf_camp_ex                                |          1 |        731 |
| rj      | inf_camp_exp                               |          9 |       3778 |
| rj      | inf_campo_e_indigena                       |          1 |       1286 |
| rj      | inf_curriculo                              |          4 |       2042 |
| rj      | inf_diversidade_etnico_racial              |          1 |        507 |
| rj      | inf_e_ef_apresentacao                      |          4 |       2437 |
| rj      | inf_e_ef_intro                             |          7 |       5544 |
| rj      | inf_espacos                                |          1 |        777 |
| rj      | inf_formacao_de_professores                |          1 |        861 |
| rj      | inf_formacao_leitora                       |          1 |        728 |
| rj      | inf_intro                                  |          6 |       4337 |
| rj      | inf_ludico                                 |          1 |        662 |
| rj      | inf_natureza                               |          3 |       1943 |
| rj      | inf_provinha                               |          1 |       1041 |
| rj      | inf_respeito_e_diversidade                 |          1 |        928 |
| rj      | inf_transicoes                             |          2 |       1207 |
| rj      | ef_ciencias_da_natureza                    |          2 |       2493 |
| rj      | ef_ciencias_humanas_geo                    |          3 |       2143 |
| rj      | ef_ciencias_humanas_his                    |          3 |       4005 |
| rj      | ef_ciencias_humanas_intro                  |          1 |       1012 |
| rj      | ef_ensino_religioso                        |          2 |       2262 |
| rj      | ef_intro                                   |          7 |       5263 |
| rj      | ef_linguagens_arte                         |          2 |       2158 |
| rj      | ef_linguagens_ed_fis                       |          3 |       3012 |
| rj      | ef_linguagens_ingles                       |          2 |       1520 |
| rj      | ef_linguagens_intro                        |          1 |        734 |
| rj      | ef_linguagens_lp                           |          2 |       3121 |
| rj      | ef_matematica                              |          3 |       2546 |
| rj      | em                                         |         13 |       8327 |
| rn      | inf                                        |         41 |      31488 |
| rn      | ef                                         |         61 |      39892 |
| rn      | em                                         |         47 |      40839 |
| ro      | inf                                        |         53 |      29869 |
| ro      | ef                                         |        110 |      85848 |
| ro      | em                                         |        116 |     135988 |
| rr      | inf                                        |         26 |      13140 |
| rr      | inf_e_ef                                   |          5 |       3832 |
| rr      | ef                                         |         67 |      55794 |
| rr      | em                                         |         66 |      56068 |
| rs      | inf                                        |         19 |      13799 |
| rs      | inf_e_ef                                   |         19 |       9654 |
| rs      | ef                                         |         12 |       9995 |
| rs      | em                                         |         91 |      73713 |
| sc      | inf_e_ef                                   |         38 |      53801 |
| sc      | em                                         |         80 |     152976 |
| se      | inf                                        |          9 |       8858 |
| se      | inf_e_ef                                   |          3 |       5201 |
| se      | ef                                         |         24 |      18676 |
| se      | em                                         |         32 |      36775 |
| sp      | inf_agrupamentos                           |          1 |        341 |
| sp      | inf_aspectos_pedagogicos                   |          1 |        527 |
| sp      | inf_avaliacao                              |          1 |        385 |
| sp      | inf_concepcao_de_infancia                  |          1 |        520 |
| sp      | inf_curriculo_e_ppp                        |          1 |        334 |
| sp      | inf_direitos_de_aprendizagem               |          1 |        965 |
| sp      | inf_e_ef_apresentacao                      |          1 |        368 |
| sp      | inf_e_ef_intro                             |         10 |       6456 |
| sp      | inf_finalidade                             |          1 |       1080 |
| sp      | inf_funcao_social                          |          1 |        437 |
| sp      | inf_papel_do_professor                     |          1 |        635 |
| sp      | inf_transicoes                             |          1 |        558 |
| sp      | ef_ciencias_da_natureza                    |          3 |       2503 |
| sp      | ef_ciencias_humanas_geo                    |          4 |       4465 |
| sp      | ef_ciencias_humanas_his                    |          2 |       2203 |
| sp      | ef_ciencias_humanas_intro                  |          1 |        529 |
| sp      | ef_ensino_religioso                        |          3 |       3040 |
| sp      | ef_intro                                   |          3 |       2511 |
| sp      | ef_linguagens_arte                         |          4 |       3086 |
| sp      | ef_linguagens_ed_fis                       |          3 |       3928 |
| sp      | ef_linguagens_ingles                       |          2 |       1754 |
| sp      | ef_linguagens_intro                        |          1 |        490 |
| sp      | ef_linguagens_lp                           |          5 |       5761 |
| sp      | ef_matematica                              |          6 |       4784 |
| sp      | em                                         |         45 |      38602 |
| to      | inf                                        |         31 |      22043 |
| to      | ef                                         |         39 |      40692 |
| to      | em                                         |         75 |      57948 |
|         |                                            |            |            |
| overall | inf                                        |        512 |     425490 |
| overall | inf_10_camp_exp                            |          1 |        752 |
| overall | inf_12_camp_exp_escuta_fala                |          1 |        660 |
| overall | inf_1_concepces                            |          1 |        537 |
| overall | inf_2_principios                           |          1 |        464 |
| overall | inf_3_direitos                             |          1 |        449 |
| overall | inf_4_planejamento                         |          1 |        662 |
| overall | inf_5_acolhimento                          |          1 |       1055 |
| overall | inf_8_camp_exp                             |          1 |        738 |
| overall | inf_adaptacoes                             |          2 |        995 |
| overall | inf_agrupamentos                           |          1 |        341 |
| overall | inf_alfabetizar                            |          3 |       1642 |
| overall | inf_apresentacao                           |          1 |        880 |
| overall | inf_aspectos_pedagogicos                   |          1 |        527 |
| overall | inf_avaliacao                              |          2 |       1333 |
| overall | inf_cam_exp                                |          7 |       4852 |
| overall | inf_camp_ex                                |          1 |        731 |
| overall | inf_camp_exp                               |         12 |       6781 |
| overall | inf_campo_e_indigena                       |          1 |       1286 |
| overall | inf_campo_exp                              |          3 |       1869 |
| overall | inf_concepcao_de_infancia                  |          1 |        520 |
| overall | inf_curriculo                              |          4 |       2042 |
| overall | inf_curriculo_e_ppp                        |          1 |        334 |
| overall | inf_direitos_de_aprendizagem               |          1 |        965 |
| overall | inf_diversidade_etnico_racial              |          1 |        507 |
| overall | inf_e_ef                                   |        243 |     240327 |
| overall | inf_e_ef_apresentacao                      |          5 |       2805 |
| overall | inf_e_ef_intro                             |         24 |      18562 |
| overall | inf_ef                                     |         17 |      13784 |
| overall | inf_espacos                                |          1 |        777 |
| overall | inf_final                                  |          1 |        372 |
| overall | inf_finalidade                             |          1 |       1080 |
| overall | inf_formacao_de_professores                |          1 |        861 |
| overall | inf_formacao_leitora                       |          1 |        728 |
| overall | inf_funcao_social                          |          1 |        437 |
| overall | inf_inclusao                               |          7 |       3220 |
| overall | inf_intro                                  |         25 |      18879 |
| overall | inf_intro_14_matriz_saberes                |          1 |        555 |
| overall | inf_intro_16_temas_integradores            |          1 |       1323 |
| overall | inf_intro_19_dinamicas                     |          1 |        408 |
| overall | inf_intro_20_avaliacao                     |          1 |        554 |
| overall | inf_ludico                                 |          1 |        662 |
| overall | inf_natureza                               |          3 |       1943 |
| overall | inf_objetivos                              |          1 |        547 |
| overall | inf_organizacao                            |          2 |        709 |
| overall | inf_papel_do_professor                     |          1 |        635 |
| overall | inf_planejamento                           |          2 |       1362 |
| overall | inf_principios                             |          5 |       2554 |
| overall | inf_provinha                               |          1 |       1041 |
| overall | inf_respeito_e_diversidade                 |          1 |        928 |
| overall | inf_trajetoria                             |          1 |        619 |
| overall | inf_transicoes                             |          3 |       1765 |
| overall | ef                                         |       1076 |     951089 |
| overall | ef_anos_finais_ciencias_da_natureza        |          1 |        251 |
| overall | ef_anos_finais_linguagens_ingles           |          2 |       1117 |
| overall | ef_anos_iniciais_arte                      |          4 |       2441 |
| overall | ef_anos_iniciais_ciencias_da_natureza      |          4 |       3039 |
| overall | ef_anos_iniciais_ciencias_humanas_geo      |          2 |       2043 |
| overall | ef_anos_iniciais_ciencias_humanas_historia |          2 |       1850 |
| overall | ef_anos_iniciais_ciencias_humanas_intro    |          1 |        678 |
| overall | ef_anos_iniciais_ensino_religioso          |          2 |       1514 |
| overall | ef_anos_iniciais_linguagens_arte           |          1 |         35 |
| overall | ef_anos_iniciais_linguagens_ed_fis         |          2 |       1240 |
| overall | ef_anos_iniciais_linguagens_intro          |          4 |       2474 |
| overall | ef_anos_iniciais_linguagens_lp             |          7 |       5100 |
| overall | ef_anos_iniciais_matematica                |          3 |       3227 |
| overall | ef_ch_geo                                  |         11 |       6943 |
| overall | ef_ch_his                                  |          7 |       4734 |
| overall | ef_ciencias                                |          9 |       5329 |
| overall | ef_ciencias_da_natureza                    |          5 |       4996 |
| overall | ef_ciencias_da_natureza_intro              |          1 |        654 |
| overall | ef_ciencias_humanas_geo                    |          7 |       6608 |
| overall | ef_ciencias_humanas_his                    |          5 |       6208 |
| overall | ef_ciencias_humanas_intro                  |          5 |       3031 |
| overall | ef_ciencias_humas_intro                    |          1 |        622 |
| overall | ef_e_em_tema_integrador                    |          1 |       3320 |
| overall | ef_ensino_religioso                        |          5 |       5302 |
| overall | ef_er                                      |         10 |       5682 |
| overall | ef_intro                                   |         14 |      11599 |
| overall | ef_linguagens_arte                         |         15 |      10549 |
| overall | ef_linguagens_ed_fis                       |         19 |      14530 |
| overall | ef_linguagens_ingles                       |         18 |      10481 |
| overall | ef_linguagens_intro                        |          3 |       2219 |
| overall | ef_linguagens_lp                           |         24 |      21918 |
| overall | ef_matematica                              |         15 |      11854 |
| overall | ef_matematica_intro                        |          1 |        701 |
| overall | em                                         |       1887 |    1986142 |
| overall | unclassified                               |         24 |      40118 |
|         |                                            |            |            |
| overall | overall                                    |       4112 |    3913487 |