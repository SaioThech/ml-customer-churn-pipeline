from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("models/churn_model.joblib")


def predict_churn(customer_data: dict) -> float:
    """Return the estimated churn probability for one customer."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run 'python src/train.py' first.")

    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([customer_data])
    probability = model.predict_proba(df)[0, 1]
    return float(probability)


if __name__ == "__main__":
    print("Use predict_churn(customer_data) to score a customer.")
