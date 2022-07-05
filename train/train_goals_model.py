import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

from joblib import dump


def train_goals_model(matches: pd.DataFrame, features: list, target: str) -> dump:

    """
    Train prediction model to determine whether
    or not the total number of goals is greater than 2.5
    and export the model as well as the results of the model
    """

    X = matches[features]
    y = matches[target]

    cv = KFold(n_splits=10, random_state=42, shuffle=True)

    model = LogisticRegression()

    scores = cross_val_score(model, X, y, scoring="accuracy", cv=cv)

    average_accuracy = round(scores.mean(), 4)
    standard_deviation = round(scores.std(), 4)

    model_results = pd.DataFrame(
        [[average_accuracy, standard_deviation]],
        columns=["average_accuracy", "standard_deviation"],
    )

    model_results.to_csv("models/goals_model/goals_model_metrics.csv", index=False)

    model.fit(X, y)
    model_name = "goals_model.pkl"

    return dump(model, f"models/goals_model/{model_name}")
