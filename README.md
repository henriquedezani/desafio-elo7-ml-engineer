# Desafio Machine Learning Engineer

A função de engenheiro de machine learning consiste em criar a ponte entra a área de ciência de dados e de engenharia de software, para tanto é necessário possuir uma familiaridade com as duas áreas e saber utilizar os conhecimentos das duas áreas em conjunto para criação de **sistemas inteligentes** de qualidade. 

Este desafio pretende exercitar essa capacidade fundamental da área, o objetivo é avaliar o quão bem o candidato mobiliza seus conhecimentos de ambos os campos na construção de um sistema inteligente simples. 

A tarefa pode ser dividida em duas partes: A criação de um **pipeline de treinamento** para um modelo de categorização de produtos e o desenvolvimento de uma **API** para servir o modelo treinado.

## Treinamento

Na primeira parte do teste, você deve desenvolver uma pipeline de treinamento para um **modelo de categorização** de produtos. Mais especificamente, você deverá treinar um modelo que recebe dados relacionados a produtos e devolve a melhor categoria para cada um deles. A sua pipeline deve conter os seguintes passos:

1. **Extração de dados**: Os dados precisam ser lidos de acordo com a forma que foram disponibilizados.
2. **Transformação de dados**: Os dados precisam ser tratados e processados para se tornarem entradas de um modelo.
3. **Modelagem**: É necessário escolher um modelo adequado que represente o problema proposto.
4. **Validadção do modelo**: O modelo precisa ser metrificado de maneira coerente com o problema a ser resolvido para medir sua qualidade.
5. **Exportação do modelo**: O modelo precisa ser disponibilizado para outros sistemas que o utilizarão.

A pipeline de treinamento deve ser implementada usando um **notebook [Jupyter][3]** em um arquivo nomeado `treinamento.ipynb`.

Não é esperado o uso de modelos complexos ou sofisticados, pois o problema pode ser resolvido com modelos simples, tais como uma regressão logística. O objetivo principal é o desenvolvimento de um processo de treino bem documentado, seguindo boas práticas tanto de [código limpo][1] quanto de treinamento de modelos de ciência de dados.

## Servidor

Na segunda parte do teste, você deve desenvolver uma **API** que receberá os dados de um conjunto de **produtos** e retornará a melhor **categoria** que o modelo pré-treinado encontrar para cada um deles. A sua aplicação deverá atender os seguintes requisitos:

1. **Carregar o modelo criado pela pipeline**: A aplicação deve carregar o modelo como parte de sua inicialização.
2. **Possuir um endpoint de categorização**: A aplicação deve possuir um endpoint de tipo **POST** `/v1/categorize` que recebe um JSON com os dados de um conjunto de produtos e retorna um JSON com as categorias preditas para cada um deles.
3. **Validar os dados de entrada**: A aplicação deve continuar funcionando e retornar o status **HTTP** `400 (Bad Request)` ao receber dados inválidos.

A aplicação deve ser construída com o uso da biblioteca Flask ou similares com um arquivo principal nomeado `api.py`.

Espera-se que o código desenvolvido siga boas práticas de [código limpo][1], **utilize testes automatizados** relevantes e documente bem seu código. Lembrando que uma boa documentação não se trata de "como" e sim de "por que".

## Detalhes de implementação, dicas e sugestões

- Espera-se que o projeto inteiro seja desenvolvido em **Python 3.9**.
- Os dados base a serem utilizados se encontram neste [link de dados públicos do elo7][2].
- O uso de [docker][5] e [docker-compose][6] para a infraestrutura de desenvolvimento do projeto é recomendado mas não exigido. 
- Este [repositório][4] oferece uma estrutura suficiente para a resolução do desafio, sinta-se a vontade para fazer um fork dele.
- A entrada da API deve seguir a seguinte estrutura básica, com um array de produtos que contém todos os campos que seu modelo utiliza:
```
{
  "products": [
    {
      "title": "Lembrancinha"
    },
    {
      "title": "Carrinho de Bebê"
    }
  ]
}
```
- A saída da API deve retornar as categorias encontradas para cada produto na mesma ordem com que foram enviados na entrada, da seguinte forma:
```
{
  "categories": [
    "Lembrancinha",
    "Bebê"
  ]
}
```

Boa sorte e divirta-se! Qualquer dúvida sinta-se a vontade para mandar um email para nós.

[1]: https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29
[2]: https://elo7-datasets.s3.amazonaws.com/data_scientist_position/elo7_recruitment_dataset.csv
[3]: https://jupyter.org/
[4]: https://github.com/renatocf/intelligent-systems-project/tree/exercise-2
[5]: https://docs.docker.com/get-docker/
[6]: https://docs.docker.com/compose/install/