from functools import lru_cache 
from define import Frontend
import questionary
import sys
from enum import Enum
import requests
class Messages(Enum):
    MENU = "Select option"
    ADD  = "Input good's name" 

@lru_cache
def get_list(host: str, port: int, path: str, params: dict):
    response = requests.get(f'http//:{host}:{port}/{path}',params)
    return response




class UserFrontendCLI(Frontend):
    
    def __init__(self, token: str, host: str, port: int):
        self.OPTIONS = { 
            "Добавить товар": self.add,
            "Получить информацию о товаре": self.get,
            "Получить список товаров": self.list,
            "Удалить товар": self.delete,
            "Получить колличество товара": self.count_of,
            "Выйти из программы": self.exit
        }
        self.host = host
        self.port = port

    def exit(self, code = 0):
        return sys.exit(code)

    def menu(self):
        selected_option = questionary.select(Messages.MENU.value, self.OPTIONS).ask() 
        option = self.OPTIONS.get(selected_option)
        return option()

    def add(self):
        ...

    def list(self):
        ...

    def delete(self):
        ...

    def get(self):
        ...
    
    def count_of(self):
        ...
