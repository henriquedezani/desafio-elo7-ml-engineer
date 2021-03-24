# Servidor

Nesta etapa foi desenvolvido uma  **API** que recebe dados de um conjunto de **produtos** e retornar a melhor **categoria** que o modelo pré-treinado encontrou para cada um deles.

## Componentes da API

1. **Carrega o modelo criado pela pipeline**: <br>
   A aplicação carrega a pipeline de aprendizado de máquina disponível na variável de ambiente `MODEL_PATH` como parte de sua inicialização.

2. **Define um endpoint de categorização**:<br>
   A aplicação disponibiliza um endpoint `/v1/categorize` (**POST**) que recebe um JSON (JavaScript Object Notation) com os dados de um conjunto de produtos e retorna um JSON com as categorias preditas para cada um deles.

3. **Validação dos dados de entrada**:<br>
   A aplicação, ao receber dados inválidos, continua funcionando e retorna o status **HTTP** `400 (Bad Request)`. Além do retorno 400 ao usuário, o sistema também armazena o log das falhas no arquivo definido na variável de ambiente `LOGGING_PATH`.

A aplicação foi construída usando a biblioteca Flask e está disponível no arquivo [api.py][1].

## Exemplo

A entrada da API consiste em um array de produtos contendo todos os campos que o modelo utilizou:
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

E a saída produzida contempla um array com as categorias encontradas para cada produto na mesma ordem com que foram enviados na entrada, da seguinte forma:
```
{
  "categories": [
    "Lembrancinha",
    "Bebê"
  ]
}
```

## Execução do ambiente 

Utilizou-se um container Docker para criar o ambiente de desenvolvimento, teste e execução da API. Veja as configurações nos arquivos [Dockerfile][2] e [docker-compose.yml][3].

Para carregar o container, basta executar o comando:

```bash
docker-compose up --build
```

A API estará disponível na porta 5000, a qual pode ser alterada no arquivo [docker-compose.yml][3].

## Execução do testes

Os testes estão disponíveis no arquivo [test.py][4] e contemplam:
- carregamento do modelo a partir da variáve de ambiente `MODEL_PATH`.
- execução da transformação do texto em vetor usando o modelo carregado.
- execução da classificação de categorias.
- invocação do endpoint com sucesso (200) (entrada correta).
- invocação do endpoint com falha (400) (entrada inválida).
- execução do endpoint com uma entrada válida.

Para execução dos testes da API, basta executar o comando abaixo quando o container já estiver sido carregado.

```bash
docker container exec -it server python test.py
```

[1]: ./api.py
[2]: ./Dockerfile
[3]: ./docker-compose.yml
[4]: ./test.py