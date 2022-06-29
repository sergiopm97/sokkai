import pandas as pd


def extract_training_data(matches: pd.DataFrame, columns: dict) -> pd.DataFrame:

    """
    Extract games played in the 2021
    season or earlier as training data
    """

    return matches[matches[columns["season"]] < 2022]
