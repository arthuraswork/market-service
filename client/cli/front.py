from texttable import Texttable
from define import Frontend
import questionary
import sys
from enum import Enum
import requests
import json
class Messages(Enum):
    MENU = "Select option"
    ADD  = "Input good's name"
    GET  = "Input good's name"

def get_list_from_server(host: str, port: int, token: str, path: str = 'v1/list'):
    response = requests.get(f'http://{host}:{port}/{path}?token={token}', stream=True)
    for j in response.iter_lines():
        if j:
            yield json.loads(j)
    response.close()


def get_object_from_server(host: str, port: int, token: str, value: str, by: str = 'title', path: str = 'v1/info'):
    response = requests.put(f'http://{host}:{port}/{path}?token={token}&by={by}&value={value}')
    obj = response.json()
    response.close()
    return obj

def incr_minus_to_server(host: str, port: int, token: str, value: str, by: str = 'title', path: str = 'v1/incr_minus'):
    response = requests.put(f'http://{host}:{port}/{path}?token={token}&by={by}&value={value}')
    code = str(response.status_code)
    response.close()
    return code

def incr_plus_to_server(host: str, port: int, token: str, value: str, by: str = 'title', path: str = 'v1/incr_plus'):
    response = requests.put(f'http://{host}:{port}/{path}?token={token}&by={by}&value={value}')
    code = str(response.status_code)
    response.close()
    return code


class UserFrontendCLI(Frontend):
    
    def __init__(self, token: str = 'test-token-market-service', host: str = 'localhost', port: int=8000):
        self.OPTIONS = { 
            "Добавить товар": self.add,
            "Получить информацию о товаре": self.get,
            "Получить список товаров": self.list,
            "Удалить товар": self.delete,
            "Получить колличество товара": self.count_of,
            "Выйти из программы": self.exit
        }
        self.token = token
        self.host = host
        self.port = port
        self.list_objects = []
        self.set_objets = set()

    def exit(self, code = 0):
        return sys.exit(code)

    def menu(self):
        selected_option = questionary.select(Messages.MENU.value, self.OPTIONS).ask() 
        option = self.OPTIONS.get(selected_option)
        return option()

    def add(self):
        if not self.list_objects:
            self.list(out=False)
        input_object = questionary.autocomplete(Messages.ADD, self.list_objects).ask()
        result = incr_plus_to_server(host='localhost', port=self.port, token=self.token, value=input_object)
        sys.stdout.write(result)

    def gen_table(self, data, out = True):
        table = Texttable()
        table.set_max_width(80)
        is_first = True
        for row in data:
            if out:
                if is_first:
                    table.header(list(row.keys()))
                    is_first = False
                table.add_row(row.values())
            self.list_objects.append(row['title'])
        if out:
            return table.draw()     

    def list(self, out = True):
        result = get_list_from_server(host='localhost',port=self.port, token=self.token)
        table = self.gen_table(result, out)
        if out and table:
            sys.stdout.write(table + '\n')


    def delete(self):
        ...

    def get(self):
        if not self.list_objects:
            self.list(out=False)
        input_object = questionary.autocomplete(Messages.GET, self.list_objects).ask()
        result = get_object_from_server(host='localhost',port=self.port, token=self.token, value=input_object)
        if not result:
            sys.stdout.write('Неизвестная ошибка' + '\n')

        else:
            sys.stdout.write('Название: ' + result.get('title') + '\n')
            sys.stdout.write('Цена: '+ str(result.get('price')) + '\n')
            sys.stdout.write('Колличество' +str(result.get('count')) + '\n')
            sys.stdout.write('Категория: ' + result.get('category') + '\n')
            sys.stdout.write('Код: ' + result.get('code') + '\n')

    def count_of(self):
        ...
