# 📊 Dados

Este diretório documenta o dataset utilizado no projeto de previsão de churn.

## Dataset

**IBM Telco Customer Churn** — conjunto público de dados de uma empresa fictícia de telecomunicações.

O dataset contém informações sobre clientes, serviços contratados, valores cobrados e a variável-alvo `Churn`.

## Como obter os dados

O dataset bruto não é versionado no GitHub. Para baixá-lo automaticamente, execute na raiz do projeto:

```bash
python data/download_data.py
```

O arquivo será salvo em:

```text
data/raw/Telco-Customer-Churn.csv
```

## Variável-alvo

A variável `Churn` representa se o cliente cancelou o serviço.

- `Yes` → cliente cancelou
- `No` → cliente permaneceu

## Por que não versionar o CSV?

O projeto mantém o código e a documentação no GitHub e baixa o dataset por script, evitando armazenar o arquivo bruto no repositório.
