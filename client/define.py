from abc import ABC, abstractmethod

class Frontend(ABC):

    @abstractmethod
    def count_of():
        """
        Вывод парамметра 'колличество' объекта
        """
        ...
    @abstractmethod
    def list():
        """
        Вывод списка объектов
        """
        ...
    @abstractmethod
    def add():
        """
        Вывод изменение парамметра 'колличество' объекта на +1
        """
        ...
    
    @abstractmethod
    def get():
        """
        Вывод информации об объекте
        """
        ...

    @abstractmethod
    def delete():
        """
        Вывод изменение парамметра 'колличество' объекта на -1
        """
        ...