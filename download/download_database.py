import pandas as pd

from dotenv import dotenv_values


def download_database() -> pd.DataFrame:

    """
    Download the complete soccer match
    database and save it as a dataframe
    """

    database_url = dict(dotenv_values(".env"))["DATABASE_URL"]

    return pd.read_csv(database_url)
