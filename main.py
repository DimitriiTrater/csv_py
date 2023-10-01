from csv_manager import CsvManager, ShowState

if __name__ == "__main__":
    temp = CsvManager("test/airtravel.csv")
    temp.Show()
    temp.Info()
