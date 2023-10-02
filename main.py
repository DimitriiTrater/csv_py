from csv_manager import CsvManager, ShowState
import tests

files = [
    "test/airtravel.csv",
    "test/fordelnan.csv",
    "test/void.csv",
    "test/cities.csv",
    "test/less_5.csv",
    "test/biostats.csv"
]

if __name__ == "__main__":
    t = tests.TestCsvManagerDelNaN(files)
    t.test_delnan()
