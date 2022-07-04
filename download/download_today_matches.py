import pandas as pd

from dotenv import dotenv_values
from datetime import date


def download_today_matches(columns: dict) -> pd.DataFrame:

    """
    Download the database of soccer matches
    with those events that only occur today
    """

    database_url = dict(dotenv_values(".env"))["DATABASE_URL"]
    current_date = str(date.today())

    matches_database = pd.read_csv(database_url)

    return matches_database[matches_database[columns["date"]] == current_date]
