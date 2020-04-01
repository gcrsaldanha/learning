from typing import Iterable


class Investment:
    ...


def read_from_csv(file_path) -> Iterable[Investment]:
    ...


def read_from_database(file_path) -> Iterable[Investment]:
    ...


class FileReader:
    read_strategy = None

    def read(self, file_path) -> Iterable[Investment]:
        return self.read_strategy.read(file_path)

    def set_strategy(self, strategy):
        self.read_strategy = strategy


if __name__ == '__main__':
    input_type, file_path = 'txt', 'file.txt'  # via cmd
    fr = FileReader()

    if input_type == 'csv':
        strategy = read_from_csv
    elif input_type == 'db':
        strategy = read_from_database

    fr.set_strategy(strategy)
    value = fr.read(file_path)
