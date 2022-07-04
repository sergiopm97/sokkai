import pandas as pd

from datetime import date
from joblib import load


def generate_predictions(
    processed_features: pd.DataFrame, matches_info: pd.DataFrame
) -> pd.DataFrame.to_csv:

    """
    Generate predictions using the
    processed data from today's matches
    """

    model = load("models/winner_model/winner_model.pkl")

    predictions = pd.DataFrame(
        model.predict_proba(processed_features),
        columns=["home_probability", "draw_away_probability"],
    )

    return pd.concat([matches_info, predictions], axis=1).to_csv(
        f"predictions/{str(date.today())}_predictions.csv"
    )
