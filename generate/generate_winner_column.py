def generate_winner_column(home_score: float, away_score: float) -> int:

    """
    Generate the column containing the winner of
    the match in a binary way taking into account whether
    the home team had more goals than the away team or not
    """

    if home_score > away_score:
        return 0

    return 1
