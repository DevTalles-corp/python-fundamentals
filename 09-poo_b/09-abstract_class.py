
from abc import ABC, abstractmethod

# Clase abstracta


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("zzzz....")


animal = Animal()
