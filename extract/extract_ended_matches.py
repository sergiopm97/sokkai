import pandas as pd


def extract_ended_matches(matches: pd.DataFrame, columns: dict) -> pd.DataFrame:

    """
    Extract matches that are ended and
    therefore have a valid result available
    """

    return matches[
        (matches[columns["home_score"]].notna())
        & (matches[columns["away_score"]].notna())
    ]
