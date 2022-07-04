import pyfiglet
from rich.console import Console
from rich.status import Status

import json
import os
import time

from download import download_today_matches


if __name__ == "__main__":

    os.system("cls")

    console = Console()

    title = pyfiglet.figlet_format("SOKKAI", font="slant")
    console.print(f"[green]{title}[/green]")

    with open("config/database_columns.json") as database_columns_config:
        database_columns = json.load(database_columns_config)

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
