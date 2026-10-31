from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score
from sklearn.pipeline import Pipeline

from data_processing import load_data, prepare_data

OUTPUT_PATH = Path("reports/model_comparison.csv")


def build_models(preprocessor):
    return {
        "Logistic Regression": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
            ]
        ),
        "Random Forest": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("classifier", RandomForestClassifier(
                    n_estimators=300,
                    random_state=42,
                    class_weight="balanced",
                    n_jobs=-1,
                )),
            ]
        ),
    }


def compare_models():
    df = load_data()
    X_train, X_test, y_train, y_test, preprocessor = prepare_data(df)
    rows = []

    for name, model in build_models(preprocessor).items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)[:, 1]
        rows.append({
            "model": name,
            "precision": precision_score(y_test, predictions, zero_division=0),
            "recall": recall_score(y_test, predictions, zero_division=0),
            "f1": f1_score(y_test, predictions, zero_division=0),
            "roc_auc": roc_auc_score(y_test, probabilities),
        })

    import pandas as pd
    results = pd.DataFrame(rows).sort_values("roc_auc", ascending=False)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT_PATH, index=False)
    print(results.to_string(index=False))
    print(f"\nResultados salvos em: {OUTPUT_PATH}")


if __name__ == "__main__":
    compare_models()
