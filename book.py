from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def show_info(self):
        pass


class Book(Person):
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def borrow(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def return_book(self):
        self.__quantity += 1

    def show_info(self):
        print(f"{self.id} | {self.title} | {self.author} | {self.__quantity}")