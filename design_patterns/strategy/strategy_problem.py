from typing import Iterable

'''
Homework: read investments from a CSV file.
Challenge: make it flexible for adding new input types (JSON, txt, etc)
'''


class Investment:
    ...


class FileReader:
    def read_from_csv(self, file_path) -> Iterable[Investment]:
        pass

    def read_from_json(self, file_path) -> Iterable[Investment]:
        pass

    def read_from_txt(self, file_path) -> Iterable[Investment]:
        pass

    ...
    # Vertical scaling, harder to contribute, harder to test
    # FileReader will have to be changed every time you want to add new behavior to it
    #   - violates OpenClosed principle (entity should have its behavior changed without source code modification)


if __name__ == '__main__':
    input_type, file_path = 'txt', 'file.txt'  # via cmd
    fr = FileReader()

    if input_type == 'txt':
        value = fr.read_from_txt(file_path)
    elif input_type == 'json':
        value = fr.read_from_json(file_path)
    elif input_type == 'txt':
        value = fr.read_from_txt(file_path)
