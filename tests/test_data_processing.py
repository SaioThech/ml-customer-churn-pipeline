import pandas as pd

from src.data_processing import prepare_target


def test_prepare_target_converts_target_and_total_charges():
    df = pd.DataFrame(
        {
            "customerID": ["001"],
            "TotalCharges": ["123.45"],
            "Churn": ["Yes"],
        }
    )

    result = prepare_target(df)

    assert "customerID" not in result.columns
    assert result.loc[0, "TotalCharges"] == 123.45
    assert result.loc[0, "Churn"] == 1
