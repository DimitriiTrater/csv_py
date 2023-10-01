import enum
import csv
import random as rndm


@enum.unique
class ShowState(enum.Enum):
    """Enumerator describe state of mode in CsvManager::Show()"""
    top = 1
    bottom = 2
    random = 3


class CsvManager:
    def __init__(self, file_path):
        self.__file_path = file_path

    def Show(self,
             mode: ShowState = ShowState.top,
             rows: int = 5,
             sep: str = ","
             ) -> None:
        """Print csv to console"""
        dict_of_params = {"mode": mode,
                          "rows": rows,
                          "sep": sep}
        if (self.__check_count_of_rows()):
            self.__top(dict_of_params)
            return
        self.__check_mode(dict_of_params)

    def __check_count_of_rows(self) -> bool:
        with open(self.__file_path, "r") as file:
            if (len(list(csv.reader(file))) < 6):
                return True
            return False

    def __check_mode(self, dict_of_params: dict) -> None:
        mode = dict_of_params["mode"]
        if (mode == ShowState.top):
            self.__top(dict_of_params)
        elif (mode == ShowState.bottom):
            self.__bottom(dict_of_params)
        elif (mode == ShowState.random):
            self.__random(dict_of_params)
        else:
            raise ValueError("Bad mode value")

    def __top(self, dict_of_params: dict) -> None:
        with open(self.__file_path, "r") as file:
            rows = list(csv.reader(file))
            print("- " * 20)
            print(*rows[0])
            print("- " * 20)
            try:
                for index in range(1, dict_of_params["rows"]+1):
                    print(*rows[index], sep=dict_of_params["sep"])
            except IndexError:
                print("Строк недостаточно")

    def __bottom(self, dict_of_params: dict) -> None:
        with open(self.__file_path, "r") as file:
            rows = list(csv.reader(file))
            print("- " * 20)
            print(*rows[0])
            print("- " * 20)
            for index in range(len(rows) - dict_of_params["rows"]-1,
                               len(rows)):
                print(*rows[index], sep=dict_of_params["sep"])

    def __random(self, dict_of_params: dict) -> None:
        with open(self.__file_path, "r") as file:
            rows = list(csv.reader(file))
            print("- " * 20)
            print(*rows[0])
            print("- " * 20)
            for _ in range(1, dict_of_params["rows"]):
                print(*rows[rndm.randint(1, len(rows)-1)],
                      sep=dict_of_params["sep"])
