import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from joblib import dump


def train_winner_model(
    matches: pd.DataFrame, target: str
) -> GradientBoostingClassifier:

    """
    Train prediction model to determine the winner of the matches
    and export the model as well as the results of the model
    """

    X = matches.drop(target, axis=1)
    y = matches[target]

    cv = KFold(n_splits=10, random_state=42, shuffle=True)

    model = GradientBoostingClassifier()

    scores = cross_val_score(model, X, y, scoring="accuracy", cv=cv)

    average_accuracy = round(scores.mean(), 4)
    standard_deviation = round(scores.std(), 4)

    model_results = pd.DataFrame(
        [[average_accuracy, standard_deviation]],
        columns=["average_accuracy", "standard_deviation"],
    )

    model_results.to_csv("models/winner_model/winner_model_metrics.csv", index=False)

    model.fit(X, y)
    model_name = "winner_model.pkl"

    return dump(model, f"models/winner_model/{model_name}")
