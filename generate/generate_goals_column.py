def generate_goals_column(home_score: float, away_score: float) -> int:

    """
    Generate goals column based on the
    logic of whether or not the sum of home
    and away team goals is greater than 2.5
    """

    if home_score + away_score <= 2:
        return 0

    else:
        return 1
