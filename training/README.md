# Treinamento

Seguindo as instruções do desafio, esta é a primeira etapa do projeto e contempla a criação de um **pipeline de treinamento** para um modelo de **classificação de categorias**, o qual recebe como **entrada um conjunto de dados de produtos**, contendo seus títulos, e **retorna a categoria** definida pelo modelo de aprendizado de máquina para cada um deles.

## Pipeline de Treinamento

O pipeline de treinamento é composto pelas seguintes etapas:

1. **Extração dos dados** <br>
   Carrega um conjunto de dados de produtos a partir de um diretório especificado na variável de ambiente `DATASET_PATH`.

2. **Transformação dos dados** <br>
   Nesta etapa os dados são tratados e processados para se tornarem entradas válidas do modelo.

3. **Modelagem** <br>
   Esta etapa é dividida em duas partes, quais sejam:
   
   - carregar um modelo de Word Embeddings treinado anteriormente com os próprios dados do dataset da Elo7 disponibilizado usando a variável de ambiente `WORD_EMBEDDINGS_PATH`. Neste desafio, utilizou-se o CBOW (Continuous Bag of Words) para a criação das word embeddings usando a biblioteca [gensim][1]. O treinamento do modelo pode ser feito utilizando o arquivo [word-embeddings.ipynb][2].
   
   - criar três pipelines de aprendizado de máquina que contemplam a transformação do texto em vetores, usando CBOW mencionado anteriormente, e o algoritmo de aprendizado de máquina. Utilizou-se os algoritmos de Regressão Logística, indicado no desafio, além de Árvore de Decisão para demonstrar a seleção do melhor algoritmo.

4. **Validação do modelo** <br>
    Nesta etapa foram utilizadas duas abordagens para o particionamento dos dados: holdout e cross-validation. Em ambos os casos, utilizou-se `stratify` para separar os conjuntos de treinamento e teste de acordo com a quantidade de amostras de cada classe, a qual está desbalanceada. Foram geradas métricas de precisão do modelo (precisão, recall, F1-score, e acurácia) e matrizes de confusão para melhor visualização.

5. **Exportação do modelo** <br>
   A partir dos scores de teste gerados na etapa de validação cruzada, definiu-se o melhor algoritmo para representar o sistema de classificação de categorias. O pipeline (contendo a transformação dos dados e o modelo de aprendizado de máquina) é então exportado para o arquivo definido na variável de ambiente `MODEL_PATH`.

## Execução do ambiente de treinamento

A infraestrutura para execução do ambiente de treinamento contempla um JupyterLab sendo executado num container Docker. Veja as configurações nos arquivos [Dockerfile][3] e [docker-compose.yml][4].

Por fim, para abrir o JupyterLab, basta executar o comando:

```bash
docker-compose up --build
```

O link estará disponível após o carregamento do container.

[1]: https://pypi.org/project/gensim/
[2]: ./word-embeddings.ipynb
[3]: ./Dockerfile
[4]: ./docker-compose.yml