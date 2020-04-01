from abc import abstractmethod
from typing import Iterable


class Investment:
    ...


class ReadStrategy:  # Interface
    @abstractmethod
    def read(self, file_path) -> Iterable[Investment]:
        ...


class ReadFromCSV(ReadStrategy):
    def read(self, file_path) -> Iterable[Investment]:
        pass


class ReadFromDatabase(ReadStrategy):
    def read(self, file_path) -> Iterable[Investment]:
        '''
        SELECT * FROM investments;
        '''
        ...


class ReadFromCSV(ReadStrategy):
    ...


class FileReader:  # Context
    read_strategy: ReadStrategy

    def read(self, file_path) -> Iterable[Investment]:
        return self.read_strategy.read(file_path)

    def set_strategy(self, strategy: ReadStrategy):
        self.read_strategy = strategy


if __name__ == '__main__':
    input_type, file_path = 'txt', 'file.txt'  # via cmd
    fr = FileReader()

    if input_type == 'csv':
        strategy = ReadFromCSV()
    elif input_type == 'db':
        strategy = ReadFromDatabase()

    fr.strategy = strategy
    value = fr.read(file_path)
