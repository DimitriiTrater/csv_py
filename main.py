from csv_manager import CsvManager, ShowState
import tests

files = [
    "test/airtravel.csv",
    "test/void.csv",
    "test/cities.csv",
    "test/less_5.csv",
    "test/biostats.csv"
]

if __name__ == "__main__":
    tShow = tests.TestCsvManagerShow(files)
    tShow.launch_tests()
