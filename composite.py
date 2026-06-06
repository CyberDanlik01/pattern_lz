#Вариант 4
class File:
    def __init__(self, name):
        self.name = name

    def show(self, space=""):
        print(f"{space} Файл: {self.name}")

class Folder:
    def __init__(self, name):
        self.name = name 
        self.content = []
    def add(self, item):
        self.content.append(item)

    def show(self, space=""):
        print(f"{space} Папка: [{self.name}]")
        for item in self.content:
            item.show(space + "  ")
