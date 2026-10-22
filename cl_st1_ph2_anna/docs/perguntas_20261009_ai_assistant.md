## Me
Relativo ao documento `perguntas_20261009.md` em anexo, pergunta 9 (Informações que precisam ser preenchidas), uma interação anterior com o AI Assistant concluiu que o método de extração dos fatores (aquela referente à análise fatorial preliminar, antes da análise fatorial rotacionada) foi `Principal Components`. A resposta foi baseada no script SAS `cl_st1_ph2_anna.sas` em anexo. Você poderia revisar, por favor?

## AI Assistant
Sim, revisei. A resposta anterior está **parcialmente correta**, mas precisa de uma formulação mais cuidadosa.

Para a **análise fatorial preliminar, não rotacionada**, isto é, a etapa usada para obter autovalores, scree plot e comunalidades iniciais, o script usa:

```
proc factor ... 
    method=principal
    plots=scree
    mineigen=1
    ...
    nfactors=100
    ...
;
```


Portanto, para essa etapa, a resposta **“Principal Components”** é defensável, porque o procedimento foi executado com `METHOD=PRINCIPAL` e sem especificar `PRIORS=`. Em termos práticos, essa etapa corresponde à extração pelo método principal/componentes principais no `PROC FACTOR`.

No entanto, há uma nuance importante: a **solução fatorial final rotacionada** não é exatamente a mesma coisa que essa etapa preliminar. Na etapa final, o script usa:

```
proc factor ...
    method=principal
    mineigen=0
    priors=max
    nfactors=&extractfactors
    rotate=promax
    ...
;
```


Ou seja, a solução final foi extraída com `METHOD=PRINCIPAL`, mas com `PRIORS=MAX`, e depois rotacionada com **Promax**. Isso aproxima a descrição de uma **análise fatorial por método principal com comunalidades iniciais estimadas pelo maior coeficiente de correlação absoluto**, e não simplesmente de uma PCA pura com comunalidades iniciais iguais a 1.

Assim, eu não deixaria a tabela apenas como:

> Método de extração: Principal Components

Eu recomendaria substituir por algo mais preciso:

| Informação | Resposta revisada |
|---|---|
| Método de extração | Na etapa preliminar não rotacionada, foi utilizado `METHOD=PRINCIPAL` no `PROC FACTOR`, correspondente à extração por componentes principais/principal method, com `MINEIGEN=1` para inspeção dos autovalores e do scree plot. Na solução final rotacionada, também foi usado `METHOD=PRINCIPAL`, mas com `PRIORS=MAX`, isto é, com comunalidades iniciais estimadas pelo maior coeficiente de correlação absoluto. |

Se a tabela exigir uma resposta curta, eu escreveria:

> **Método principal (`METHOD=PRINCIPAL` no PROC FACTOR); na etapa preliminar, equivalente a Principal Components; na solução final, usado com `PRIORS=MAX`.**

Portanto, a conclusão anterior — **“Principal Components”** — está correta **apenas se a pergunta se refere estritamente à etapa preliminar não rotacionada**. Para a metodologia completa, é melhor registrar a nuance do `PRIORS=MAX` na solução final.

## Me
Muito obrigado! Então, a resposta está correta, pois a pergunta se referia à etapa anterior não rotacionada.

Eu fiquei em dúvida porque, aparentemente, me confundi com o parâmetro `PRINCIPAL` na `PROC FACTOR` com a análise `Principal Components Analysis`, que difere da `Factor Analysis`. Você poderia ajudar a esclarecer isso?

## AI Assistant
Claro. A sua dúvida é muito pertinente, porque a nomenclatura do **`PROC FACTOR` do SAS** pode ser confusa: ele oferece um método chamado `PRINCIPAL`, mas isso não significa necessariamente que toda a análise deva ser descrita, conceitualmente, como “PCA” no sentido estrito em oposição à “Factor Analysis”.

A forma mais simples de entender é esta:

> **PCA e Factor Analysis são modelos conceitualmente diferentes, mas o SAS `PROC FACTOR` permite usar um método de extração chamado `PRINCIPAL`, que pode funcionar de modo muito próximo à PCA quando as comunalidades iniciais são 1.**

## 1. Diferença conceitual entre PCA e análise fatorial

### Principal Components Analysis — PCA

A **PCA** é uma técnica de redução de dimensionalidade. Ela transforma um conjunto de variáveis observadas em componentes lineares que procuram explicar a maior quantidade possível da **variância total** das variáveis.

Em termos simples:

> A PCA resume muitas variáveis observadas em poucos componentes, usando toda a variância disponível: variância comum, variância específica e erro.

Na PCA, cada variável é tratada como tendo comunalidade inicial igual a **1**, isto é, assume-se que 100% da variância da variável está disponível para ser explicada pelos componentes.

Por isso, a PCA é frequentemente descrita como uma técnica de **data reduction**, ou redução de dados.

### Factor Analysis — análise fatorial comum

A **análise fatorial**, em sentido mais estrito, parte de outro modelo. Ela procura explicar as correlações entre variáveis observadas por meio de fatores latentes subjacentes.

Em termos simples:

> A análise fatorial procura identificar fatores não observados que explicam a variância compartilhada entre as variáveis.

Nesse caso, nem toda a variância das variáveis é considerada relevante para a solução fatorial. A análise separa, pelo menos conceitualmente:

- **variância comum**: compartilhada com outras variáveis;
- **variância específica**: própria daquela variável;
- **erro**: ruído ou variância não explicada.

Por isso, na análise fatorial comum, as comunalidades iniciais geralmente são menores que 1, porque a análise tenta modelar apenas a parte compartilhada da variância.

## 2. Onde entra o `METHOD=PRINCIPAL` do SAS?

No `PROC FACTOR`, `METHOD=PRINCIPAL` é um **método de extração**. Ele é chamado de “principal factor method” ou “principal components method” dependendo das comunalidades usadas.

A questão decisiva é: **quais são as comunalidades iniciais?**

### Caso A: `METHOD=PRINCIPAL` sem `PRIORS=`

Quando você usa:

```
proc factor method=principal;
run;
```


e não especifica `PRIORS=`, o SAS usa, por padrão, comunalidades iniciais iguais a **1**.

Isso torna a extração equivalente, na prática, a uma **análise de componentes principais** aplicada à matriz de correlações.

Por isso, para a etapa preliminar não rotacionada do seu caso, a resposta **“Principal Components”** está correta.

### Caso B: `METHOD=PRINCIPAL` com `PRIORS=MAX`, `PRIORS=SMC`, etc.

Quando se usa algo como:

```
proc factor method=principal priors=max;
run;
```


a situação muda. O método continua sendo `METHOD=PRINCIPAL`, mas as comunalidades iniciais já não são fixadas em 1. Elas são estimadas por algum critério, por exemplo:

- `PRIORS=MAX`: maior correlação absoluta da variável com outra variável;
- `PRIORS=SMC`: squared multiple correlation;
- outros métodos de estimação de comunalidade.

Nesse caso, a análise se aproxima mais de uma **análise fatorial comum**, porque a matriz analisada tem a diagonal substituída por estimativas de comunalidade, e não por 1.

Então, o mesmo `METHOD=PRINCIPAL` pode aparecer em dois usos levemente diferentes:

| Situação | Diagonal/comunalidade inicial | Interpretação |
|---|---:|---|
| `METHOD=PRINCIPAL` sem `PRIORS=` | 1 | PCA / componentes principais |
| `METHOD=PRINCIPAL` com `PRIORS=` menor que 1 | comunalidades estimadas | método principal de análise fatorial comum |

## 3. Então `PRINCIPAL` no SAS é PCA ou Factor Analysis?

A resposta curta é:

> **Depende das comunalidades iniciais.**

Mais precisamente:

- se a diagonal da matriz de correlações é composta por **1s**, o procedimento é equivalente à **Principal Components Analysis**;
- se a diagonal é composta por **estimativas de comunalidade**, o procedimento é mais propriamente uma **principal factor analysis** ou **principal axis/principal factor extraction**, dependendo da terminologia adotada.

É por isso que a confusão é comum. O nome `PRINCIPAL` no SAS não resolve sozinho a distinção teórica entre PCA e análise fatorial comum. É preciso verificar se houve `PRIORS=`.

## 4. No seu caso específico

Na etapa **preliminar, não rotacionada**, usada para examinar autovalores, scree plot e comunalidades, foi usado `METHOD=PRINCIPAL` **sem `PRIORS=`**.

Portanto, nessa etapa:

> **A extração foi por componentes principais, isto é, Principal Components.**

Já na etapa final rotacionada, foi usado `METHOD=PRINCIPAL` com `PRIORS=MAX`, então a formulação mais precisa para essa parte seria:

> **extração pelo método principal com comunalidades iniciais estimadas por `PRIORS=MAX`, seguida de rotação Promax.**

Mas como a pergunta 9 se referia explicitamente à etapa preliminar não rotacionada, a resposta **Principal Components** está adequada.

## 5. Uma formulação metodológica segura

Se você quiser evitar ambiguidade na tese, eu sugeriria escrever algo assim:

> Na etapa exploratória preliminar, anterior à rotação, utilizou-se o `PROC FACTOR` do SAS com `METHOD=PRINCIPAL`, sem especificação de comunalidades iniciais alternativas. Desse modo, as comunalidades iniciais foram tratadas como iguais a 1, caracterizando uma extração por componentes principais. Essa etapa foi utilizada para examinar os autovalores, o scree plot e subsidiar a decisão sobre a retenção de fatores. Na etapa posterior, a solução final foi estimada com `METHOD=PRINCIPAL` e comunalidades iniciais definidas por `PRIORS=MAX`, seguida de rotação Promax.

Se a Anna precisar de uma resposta curta para a tabela, pode ficar assim:

> **Principal Components na etapa preliminar não rotacionada (`METHOD=PRINCIPAL` sem `PRIORS=` no `PROC FACTOR`).**

## 6. Resumo em uma frase

A sua interpretação está correta: **PCA e análise fatorial são conceitualmente diferentes**, mas, no `PROC FACTOR` do SAS, `METHOD=PRINCIPAL` sem `PRIORS=` executa uma extração equivalente à **Principal Components Analysis**, razão pela qual a resposta “Principal Components” é correta para a etapa preliminar não rotacionada.
