import pandas as pd
from sklearn.preprocessing import StandardScaler


def process_features(matches: pd.DataFrame, features: list) -> pd.DataFrame:

    """
    Process the independent columns using
    a numerical scaler called Standard Scaler
    """

    scaler = StandardScaler().fit(matches[features])

    return scaler.transform(matches[features]), scaler
