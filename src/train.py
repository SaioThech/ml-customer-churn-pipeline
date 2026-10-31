from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from data_processing import load_data, prepare_data


MODEL_PATH = Path("models/churn_model.joblib")


def train():
    df = load_data()
    X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(max_iter=1000, class_weight="balanced"),
            ),
        ]
    )

    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Modelo treinado com sucesso.")
    print(f"Arquivo salvo em: {MODEL_PATH}")
    print(f"Treino: {len(X_train)} registros")
    print(f"Teste: {len(X_test)} registros")


if __name__ == "__main__":
    train()
