# 🤖 ML Customer Churn Pipeline

Projeto de Machine Learning para prever a probabilidade de um cliente cancelar um serviço (churn).

Este projeto faz parte da minha evolução prática como **AI Engineer**, conectando análise de dados, pré-processamento, treinamento, avaliação, comparação de modelos e organização de um pipeline reproduzível.

## 🎯 Objetivo

Construir um pipeline de ponta a ponta capaz de:

- carregar e preparar dados;
- explorar o comportamento dos clientes;
- transformar variáveis categóricas e numéricas;
- treinar modelos de classificação;
- comparar modelos;
- avaliar desempenho com métricas de classificação;
- gerar previsões de churn;
- automatizar verificações com GitHub Actions.

## 🧠 Pipeline

```text
Dataset
  ↓
Análise exploratória
  ↓
Limpeza e preparação
  ↓
Train / Test Split
  ↓
Pré-processamento
  ↓
Treinamento
  ↓
Comparação de modelos
  ↓
Avaliação
  ↓
Predição de Churn
```

## 🛠️ Tecnologias

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook
- Pytest
- GitHub Actions

## 📂 Estrutura

```text
ml-customer-churn-pipeline/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── data/
│   ├── README.md
│   └── download_data.py
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── src/
│   ├── data_processing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── compare_models.py
│   └── predict.py
├── tests/
│   └── test_data_processing.py
├── models/
│   └── .gitkeep
├── reports/
│   └── README.md
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset

O projeto utiliza o **IBM Telco Customer Churn**, um dataset público com informações de clientes, serviços contratados, valores cobrados e a variável-alvo `Churn`.

O CSV bruto não é versionado no GitHub. Para obter os dados:

```bash
python data/download_data.py
```

## 🔬 Modelos

O projeto começa com **Logistic Regression** como baseline e também possui uma etapa de comparação com **Random Forest**.

A comparação considera principalmente:

- Precision
- Recall
- F1-score
- ROC-AUC

Os resultados reais são gerados somente após a execução do pipeline, evitando números inventados no README.

## 🚀 Como executar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar no Windows

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Baixar o dataset

```bash
python data/download_data.py
```

### 5. Treinar o modelo baseline

```bash
python src/train.py
```

### 6. Avaliar

```bash
python src/evaluate.py
```

### 7. Comparar modelos

```bash
python src/compare_models.py
```

### 8. Executar testes

```bash
pytest -q
```

## ⚙️ Integração contínua

O projeto possui um workflow de **GitHub Actions** que instala as dependências, verifica a sintaxe Python e executa os testes a cada alteração na branch principal ou pull request.

## 📈 Próximas evoluções

- análise de importância das variáveis;
- ajuste de hiperparâmetros;
- API para predição;
- Docker;
- monitoramento de modelo;
- evolução para uma arquitetura de ML próxima de produção.

## 👩🏽‍💻 Sobre mim

Sou estudante de Inteligência Artificial e Machine Learning, construindo minha trajetória como **AI Engineer**.

Meu objetivo é desenvolver sistemas de IA de forma prática, passando por dados, Machine Learning, NLP, LLMs, RAG e engenharia de sistemas de IA.

🔗 [GitHub](https://github.com/SaioThech)
