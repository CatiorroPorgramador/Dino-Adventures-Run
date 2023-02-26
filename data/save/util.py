import json
from json import dump, load

def write_json(file_name, data: dict):
    with open(file_name, 'w', encoding='utf8') as file:
        dump(data, file)

def read_json(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        return load(file)