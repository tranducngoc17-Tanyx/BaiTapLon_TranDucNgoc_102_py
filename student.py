from book import Person

class Student(Person):
    def __init__(self, id, name, class_name):
        self.id = id
        self.name = name
        self.class_name = class_name

    def show_info(self):
        print(f"{self.id} | {self.name} | {self.class_name}")