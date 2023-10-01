from csv_manager import CsvManager, ShowState
from typing import List


class TestCsvManagerShow:
    def __init__(self, files: List):
        self.files = files

    def top_f_zero_t_hundred(self):
        for i in self.files:
            temp = CsvManager(i)
            for j in range(0, 101):
                temp.Show(mode=ShowState.top, rows=j)

    def bottom_f_zero_t_hundred(self):
        for i in self.files:
            temp = CsvManager(i)
            for j in range(0, 101):
                temp.Show(mode=ShowState.bottom, rows=j)

    def random_f_zero_t_hundred(self):
        for i in self.files:
            temp = CsvManager(i)
            for j in range(0, 101):
                temp.Show(mode=ShowState.random, rows=j)

    def launch_tests(self):
        self.top_f_zero_t_hundred()
        self.bottom_f_zero_t_hundred()
        self.random_f_zero_t_hundred()