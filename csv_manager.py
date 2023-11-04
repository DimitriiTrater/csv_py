import enum
import csv
import random as rndm
from copy import deepcopy
import os


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
        if (self.__check_count_of_rows(rows)):
            self.__top(dict_of_params)
            return
        self.__check_mode(dict_of_params)

    def __check_count_of_rows(self, rows: int) -> bool:
        with open(self.__file_path, "r") as file:
            if (len(list(csv.reader(file))) < rows):
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
            rows = deepcopy(list(csv.reader(file)))
            header = rows.pop(0)
            print("- " * 20)
            print(*header)
            print("- " * 20)
            for index in range(len(rows) - dict_of_params["rows"],
                               len(rows)):
                print(*rows[index], sep=dict_of_params["sep"])

    def __random(self, dict_of_params: dict) -> None:
        with open(self.__file_path, "r") as file:
            rows = list(csv.reader(file))
            print("- " * 20)
            print(*rows[0])
            print("- " * 20)
            for _ in range(1, dict_of_params["rows"]+1):
                print(*rows[rndm.randint(1, len(rows)-1)],
                      sep=dict_of_params["sep"])

    def Info(self) -> None:
        with open(self.__file_path, "r") as file:
            rows = deepcopy(list(csv.reader(file)))
            header = rows.pop(0)
            rows_with_data = list(x for x in rows if x != [])
            count_of_rows_with_data = len(rows_with_data)
            print("Количество строк с данными на количество столбцов:")
            print(f"{count_of_rows_with_data}x{len(header)}")
            for i in range(len(header)):
                count_of_columns_with_data = sum(
                    1 for x in rows_with_data if x[i].replace(
                        " ", ""
                    ) != ""
                )
                h = header[i].replace(" ", "")
                t = self.__get_type_of_var(rows_with_data[0][i])
                print(f"{h} {count_of_columns_with_data} {t}")

    def __get_type_of_var(self, var) -> str:
        try:
            new_var = float(var)
        except ValueError:
            return "string"
        if (new_var - int(new_var) == 0):
            return "int"
        return "float"

    def DelNaN(self):
        with open(self.__file_path, "r") as file:
            rows = deepcopy(list(csv.reader(file)))
            del_rows = []
            for row in rows:
                for column in row:
                    if column.replace(" ", "") == "":
                        print("NaN")
                        print(row)
                        del_rows.append(row)
                        break

            for del_row in del_rows:
                rows.remove(del_row)

            res = open("result.csv", "w")
            res_writer = csv.writer(res)
            for row in rows:
                res_writer.writerow(row)
            res.close()

    def MakeDS(self) -> None:
        with open(self.__file_path, "r") as file:
            rows = deepcopy(list(csv.reader(file)))
            header = rows.pop(0)
            len_rows = len(rows)
            rndm.shuffle(rows)
            seventy_percent = round(len_rows / 100 * 70)
            thirty_percent = len_rows - seventy_percent

            try:
                train = open("workdata/learning/train.csv", "w")
            except FileNotFoundError:
                os.mkdir("workdata/")
                os.mkdir("workdata/learning/")
                train = open("workdata/learning/train.csv", "w")
            train_writer = csv.writer(train)
            train_writer.writerow(header)
            print(header)
            for i in range(seventy_percent):
                print(rows[i])
                train_writer.writerow(rows[i])
            train.close()

            try:
                test = open("workdata/testing/test.csv", "w")
            except FileNotFoundError:
                os.mkdir("workdata/testing/")
                test = open("workdata/testing/test.csv", "w")
            test_writer = csv.writer(test)
            test_writer.writerow(header)
            print(header)
            for i in range(thirty_percent):
                print(rows[seventy_percent + i])
                test_writer.writerow(rows[seventy_percent + i])
            test.close()
