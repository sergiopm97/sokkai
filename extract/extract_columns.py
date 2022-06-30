import pandas as pd


def extract_columns(matches: pd.DataFrame, columns: dict) -> pd.DataFrame:

    """
    Extract the independent columns and the ones
    that will be used to generate the dependent column
    at the same time as we drop the remaining NaN values
    """

    return matches[list(columns.values())[6:17]].dropna()
