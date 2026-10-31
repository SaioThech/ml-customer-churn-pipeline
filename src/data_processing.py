from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path("data/raw/Telco-Customer-Churn.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the churn dataset from a CSV file."""
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Run 'python data/download_data.py' first."
        )

    return pd.read_csv(path)


def prepare_target(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the target and convert it to binary values."""
    df = df.copy()

    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    if "Churn" not in df.columns:
        raise ValueError("The dataset must contain a 'Churn' column.")

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df.dropna(subset=["Churn"])


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing for numeric and categorical features."""
    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )


def prepare_data(df: pd.DataFrame):
    """Prepare train/test data and the preprocessing transformer."""
    df = prepare_target(df)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    preprocessor = build_preprocessor(X_train)
    return X_train, X_test, y_train, y_test, preprocessor
