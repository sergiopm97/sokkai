from download import download_database
from extract import extract_training_data, extract_ended_matches, extract_columns
import json


if __name__ == "__main__":

    with open("config/database_columns.json") as database_columns_config:
        database_columns = json.load(database_columns_config)

    matches_database = download_database()

    training_matches = extract_training_data(matches_database, database_columns)
    training_ended_matches = extract_ended_matches(training_matches, database_columns)
    extracted_matches_data = extract_columns(training_ended_matches, database_columns)
