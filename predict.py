from joblib import load
import pyfiglet
import pandas as pd
from rich.console import Console
from rich.status import Status

import json
import os
import time

from download import download_today_matches
from extract import extract_columns


if __name__ == "__main__":

    os.system("cls")

    console = Console()

    title = pyfiglet.figlet_format("SOKKAI", font="slant")
    console.print(f"[green]{title}[/green]")

    with open("config/database_columns.json") as database_columns_config:
        database_columns = json.load(database_columns_config)

    match_columns_plus_info = list(database_columns.values())[0:15]
    match_features = list(database_columns.values())[6:15]

    today_matches_download_status = Status(
        "Downloading soccer matches for today[white]...[/white]"
    )

    today_matches_download_status.start()
    time.sleep(1)

    today_soccer_matches = download_today_matches(database_columns)

    today_matches_download_status.stop()

    console.print(
        "[green][OK][/green] Today soccer matches download done!",
        style="bold white",
    )

    pipeline_status = Status("Processing the data along the pipeline[white]...[/white]")

    pipeline_status.start()
    time.sleep(1)

    matches_data_plus_info = extract_columns(
        today_soccer_matches, match_columns_plus_info
    )

    matches_info_data = matches_data_plus_info.drop(columns=match_features)
    matches_features_data = matches_data_plus_info[match_features]

    scaler = load("models/winner_model/winner_scaler.pkl")

    processed_matches_data = pd.DataFrame(
        scaler.transform(matches_features_data), columns=matches_features_data.columns
    )

    pipeline_status.stop()

    console.print(
        "[green][OK][/green] Data processing along the pipeline done!",
        style="bold white",
    )
