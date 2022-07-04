import pandas as pd

from joblib import load


def process_new_data(features: pd.DataFrame) -> pd.DataFrame:

    """
    Process the features of today's matches using
    the scaler that was used in the training phase
    """

    scaler = load("models/winner_model/winner_scaler.pkl")

    return pd.DataFrame(scaler.transform(features), columns=features.columns)
