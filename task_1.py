from random import randint as rnd
from random import choice as ch

class Human:
    def __init__(self, name, age,) -> None:
        self.name = name
        self.age = age

class Parent:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.list_children = []
        
    def add_chirldren(self, other):
        if self.age - other.age > 16:
            self.list_children.append(other)
            return f"Ребенок {other.name} успешно добавлен в ваш список детей."
        else:
            return f"Возраст ребенка должен быть меньше 16 лет."
        
    def __str__(self):
        return f"My name is {self.name}.\n\
I am {self.age} years old."

    def calm_children_down(self,other):
        other.set_state_of_calm()
    
    def feed_chirldren(self, other):
        other.set_state_of_hunger()
        
    def get_info_chirldrens(self):
        for i in self.list_children:
            print(i,"\n")
    

class Kid:
    def __init__(self, name, age, state_of_calm=True, state_of_hunger=False) -> None:
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm # состояние спокойствия
        self.state_of_hunger = state_of_hunger # состояние голода
        
    def __str__(self) -> str:
        return f"Привет! Меня зовут {self.name}.\nМне {self.age} лет!\n{self.get_hunger()} и {self.show_calm()}"
        
    def set_state_of_calm(self):
        self.set_state_of_calm = True
        
    def set_state_of_hunger(self):
        self.set_state_of_hunger = False
        
    def get_hunger(self):
        return "Я не голоден" if not self.state_of_hunger else "Я голоден и очень хочу кушать"
    
    def show_calm(self):
        return "Я спокоен" if self.state_of_calm else "Мне ничего здесь не нравиться!\nЯ хочу развлечений!"
    
def fabric_chirldrens(number: int, parent: Parent) -> None:
    names = ["Иван", "Петр", "Кирилл", "Василий", "Юля", "Маша", "Варя", "Максим", "Антон", "Артем", "Маргарита", "Адам", "Федор"]
    for _ in range(number):
        age = rnd(1, 50)
        name = ch(names)
        calm = ch([True, False])
        hunger = ch([False, True])
        parent.add_chirldren(Kid(name, age, calm, hunger))



if __name__ == "__main__":
    parent = Parent("Тимофей", 42)
    list_children_parent = fabric_chirldrens(10, parent)
    print("=" * 50)
    print("=" * 50)
    print(parent)
    print("=" * 50)
    print("=" * 50)
    parent.get_info_chirldrens()