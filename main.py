from csv_manager import CsvManager, ShowState

if __name__ == "__main__":
    n = CsvManager("test/less_5.csv")
    n.Show(mode=ShowState.random)
