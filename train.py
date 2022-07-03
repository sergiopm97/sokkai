import pyfiglet
from rich.console import Console
from rich.status import Status

import json
import os
import time

from download import download_database
from extract import extract_training_data, extract_ended_matches, extract_columns
from generate import generate_winner_column
from process import process_features
from train import train_winner_model


if __name__ == "__main__":

    os.system("cls")

    console = Console()

    title = pyfiglet.figlet_format("SOKKAI", font="slant")
    console.print(f"[green]{title}[/green]")

    with open("config/database_columns.json") as database_columns_config:
        database_columns = json.load(database_columns_config)

    match_columns = list(database_columns.values())[6:17]
    match_features = list(database_columns.values())[6:15]

    database_download_status = Status(
        "Downloading soccer matches database[white]...[/white]"
    )

    database_download_status.start()
    time.sleep(1)

    matches_database = download_database()

    database_download_status.stop()

    console.print(
        "[green][OK][/green] Database download done!",
        style="bold white",
    )

    matches_data_extraction_status = Status(
        "Extracting soccer matches data[white]...[/white]"
    )

    matches_data_extraction_status.start()
    time.sleep(1)

    training_matches = extract_training_data(matches_database, database_columns)
    training_ended_matches = extract_ended_matches(training_matches, database_columns)
    extracted_matches_data = extract_columns(training_ended_matches, match_columns)

    matches_data_extraction_status.stop()

    console.print(
        "[green][OK][/green] Matches data extraction done!",
        style="bold white",
    )

    winner_column_status = Status("Generating winner column[white]...[/white]")

    winner_column_status.start()
    time.sleep(1)

    extracted_matches_data["match_winner"], match_winner_column = (
        extracted_matches_data.apply(
            lambda match: generate_winner_column(
                match[database_columns["home_score"]],
                match[database_columns["away_score"]],
            ),
            axis=1,
        ),
        "match_winner",
    )

    extracted_matches_data = extracted_matches_data.drop(
        columns=[database_columns["home_score"], database_columns["away_score"]]
    )

    winner_column_status.stop()

    console.print(
        "[green][OK][/green] Winner column generation done!",
        style="bold white",
    )

    matches_data_processing_status = Status(
        "Processing soccer matches data[white]...[/white]"
    )

    matches_data_processing_status.start()
    time.sleep(1)

    (
        extracted_matches_data[match_features],
        scaler,
    ) = process_features(extracted_matches_data, match_features)

    matches_data_processing_status.stop()

    console.print(
        "[green][OK][/green] Matches data processing done!",
        style="bold white",
    )

    winner_model_training_status = Status("Training winner model[white]...[/white]")

    winner_model_training_status.start()
    time.sleep(1)

    train_winner_model(extracted_matches_data, match_winner_column)

    winner_model_training_status.stop()

    console.print(
        "[green][OK][/green] Winner model training done!\n",
        style="bold white",
    )
