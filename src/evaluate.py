from pathlib import Path

import joblib
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from data_processing import load_data, prepare_data


MODEL_PATH = Path("models/churn_model.joblib")


def evaluate():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Run 'python src/train.py' first."
        )

    df = load_data()
    _, X_test, _, y_test, _ = prepare_data(df)
    model = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("\n=== Model Evaluation ===")
    print(f"Accuracy:  {accuracy_score(y_test, predictions):.4f}")
    print(f"Precision: {precision_score(y_test, predictions, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, predictions, zero_division=0):.4f}")
    print(f"F1-score:  {f1_score(y_test, predictions, zero_division=0):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_test, probabilities):.4f}")

    print("\n=== Classification Report ===")
    print(classification_report(y_test, predictions, zero_division=0))

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, predictions))


if __name__ == "__main__":
    evaluate()
