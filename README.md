# API de Predição de Faixa Salarial

Esta API utiliza um modelo de Machine Learning (Random Forest) para prever a faixa salarial de profissionais de dados no Brasil, com base em suas características de formação, experiência e tecnologia.

O projeto é a implementação em produção do modelo desenvolvido no trabalho acadêmico "Disparidade Salarial dos Profissionais de Dados no Brasil" da PUC Minas.

---

## Pré-requisitos

-   Docker
-   Git

## Como Executar a API

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_NO_GITHUB]
    cd api-disparidade-salarial
    ```

2.  **Construa a imagem Docker:**
    O arquivo do modelo (`model.joblib`) já está incluído. Para construir a imagem, execute:
    ```bash
    docker build -t api-salarial .
    ```

3.  **Execute o contêiner:**
    ```bash
    docker run -p 5000:5000 api-salarial
    ```
    A API estará disponível em `http://localhost:5000`.  Essa URL é o endereço local no seu próprio computador onde a sua API se torna acessível depois que você executa o contêiner Docker. 

---

## Endpoints da API

### Health Check  

Verifica se a API está em funcionamento.

-   **URL:** `/health`
-   **Método:** `GET`
-   **Resposta de Sucesso (200):**
    ```json
    {
      "status": "API está funcionando!"
    }
    ```

### Predição Salarial ⚠️= 

Realiza a predição da faixa salarial.

-   **URL:** `/predict`
-   **Método:** `POST`
-   **Corpo da Requisição (JSON):**
    ```json
    {
      "estado_onde_reside": "São Paulo (SP)",
      "idade": 30,
      "formacao_academica": "Bacharelado",
      "nivel_de_ensino_alcalcado": "Pós-graduação",
      "tempo_de_experiencia_na_area_de_dados": "de 3 a 4 anos",
      "principal_linguagem_de_programacao_utilizada": "Python",
      "plataforma_de_nuvem_mais_utilizada": "AWS"
    }
    ```
-   **Resposta de Sucesso (200):**
    ```json
    {
      "prediction": "Faixa 3",
      "confidence": {
        "classes": ["Faixa 1", "Faixa 2", "Faixa 3", "Faixa 4", "Faixa 5"],
        "probabilities": [0.1, 0.2, 0.6, 0.05, 0.05]
      }
    }
    ```

---

## Como Treinar um Novo Modelo

Para retreinar o modelo com novos dados, coloque o `dados_limpos.csv` na raiz do projeto e execute o script de treinamento.

```bash
# Certifique-se de ter um ambiente Python com as dependências do requirements.txt
python scripts/train.py
```
Isso irá gerar um novo `model.joblib` na pasta `model/`. Após isso, reconstrua a imagem Docker para que ela use o novo modelo.