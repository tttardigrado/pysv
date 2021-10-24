from pysv.functions.general import p_print
from pysv.functions.output import error_message
from typing import List
import csv
from pysv.classes.csv_file import CSVFile


def load_csv(file_path: str) -> CSVFile:
    try:
        with open(file_path, "r") as f:
            data = csv.reader(f)
            rows: List[List[str]] = [row for row in data]
            return CSVFile(header=rows[0], rows=rows[1:], path=file_path)

    except FileNotFoundError:
        p_print(error_message("That file does not exist"))
        return CSVFile([], [], "")
