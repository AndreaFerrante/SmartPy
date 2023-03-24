import json


def read_file(path_filename:str=None, mode:str='r') -> str:

    with open(path_filename, mode) as smart:
        read_file = smart.read()

    return read_file


def write_compiled_file_to_json(file_to_save, path_filename:str='', extension:str='json') -> None:

    with open(path_filename + "." + extension, "w") as file:
        json.dump(file_to_save, file)