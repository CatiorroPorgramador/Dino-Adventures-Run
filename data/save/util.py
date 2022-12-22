import json
from os import system


def write_json(file_name, data: dict):
    with open(file_name, 'w', encoding='utf8') as file:
        json.dump(data, file)


def read_json(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        return json.load(file)


def data_verification(file_name):
    data = {
        'coins': 0,
        'items': [],
    }

    try:
        print("ARQUIVO ENCONTRADO")
        file = open(file_name, 'r')

        file.close()
        return 0

    except:
        print('ARQUIVO NAO ENCONTRADO, CRIANDO NOVO ARQUIVO')
        system('md variables')
        write_json('variables/save.json', data)
        return -1
