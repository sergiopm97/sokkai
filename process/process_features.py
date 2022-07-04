import pandas as pd
from sklearn.preprocessing import StandardScaler

from joblib import dump


def process_features(matches: pd.DataFrame, features: list) -> pd.DataFrame:

    """
    Process the independent columns using
    a numerical scaler called Standard Scaler
    and export the object for future use
    """

    scaler = StandardScaler().fit(matches[features])
    scaler_name = "winner_scaler.pkl"

    dump(scaler, f"models/winner_model/{scaler_name}")

    return scaler.transform(matches[features])
