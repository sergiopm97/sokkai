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

    winner_model = load("models/winner_model/winner_model.pkl")
    goals_model = load("models/goals_model/goals_model.pkl")

    winner_predictions = pd.DataFrame(
        winner_model.predict_proba(processed_features),
        columns=["home_probability", "draw_away_probability"],
    )

    goals_predictions = pd.DataFrame(
        goals_model.predict_proba(processed_features),
        columns=["under_2.5_probability", "over_2.5_probability"],
    )

    return pd.concat(
        [matches_info, winner_predictions, goals_predictions], axis=1
    ).to_csv(f"predictions/{str(date.today())}_predictions.csv")
