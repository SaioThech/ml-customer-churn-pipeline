# 🤖 ML Customer Churn Pipeline

Projeto de Machine Learning para prever a probabilidade de um cliente cancelar um serviço (churn).

Este projeto faz parte da minha evolução prática como **AI Engineer**, conectando análise de dados, pré-processamento, treinamento, avaliação e organização de um pipeline de Machine Learning.

## 🎯 Objetivo

Construir um pipeline de ponta a ponta capaz de:

- carregar e preparar dados;
- analisar características dos clientes;
- transformar variáveis categóricas e numéricas;
- treinar modelos de classificação;
- avaliar o desempenho dos modelos;
- gerar previsões de churn;
- organizar o projeto de forma reproduzível.

## 🧠 Pipeline

```text
Dados
  ↓
Análise exploratória
  ↓
Pré-processamento
  ↓
Train / Test Split
  ↓
Treinamento
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

## 📂 Estrutura

```text
ml-customer-churn-pipeline/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── train.py
│   └── evaluate.py
│
├── models/
│   └── .gitkeep
│
├── reports/
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset

O projeto será estruturado para trabalhar com um conjunto de dados de clientes contendo informações de perfil, serviços contratados, valores pagos e indicador de churn.

A fonte e os detalhes do dataset serão documentados em `data/README.md`.

## 📈 Avaliação

As principais métricas utilizadas serão:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Matriz de confusão

**Os resultados serão adicionados após a execução do treinamento.**

## 🚀 Como executar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar treinamento

```bash
python src/train.py
```

### 5. Avaliar o modelo

```bash
python src/evaluate.py
```

## 🔬 Próximas etapas

- análise exploratória com visualizações;
- comparação entre modelos;
- ajuste de hiperparâmetros;
- análise de importância das variáveis;
- tratamento de desbalanceamento;
- criação de uma API para predição;
- containerização com Docker;
- evolução para uma arquitetura de ML mais próxima de produção.

## 👩🏽‍💻 Sobre mim

Sou estudante de Inteligência Artificial e Machine Learning, construindo minha trajetória como **AI Engineer**.

Meu objetivo é desenvolver sistemas de IA de forma prática, passando por dados, Machine Learning, NLP, LLMs, RAG e engenharia de sistemas de IA.

🔗 [GitHub](https://github.com/SaioThech)
