from random import randint as rnd


class Human:
    def __init__(self, name, home) -> None:
        self.name = name
        self.lvl_hunger = 50
        self.home = home
        
    def __str__(self):
        return f"Меня зовут {self.name}.\nМое чувство сытости составляет {self.lvl_hunger}.\n\
В моем доме {self.home.fridge} еды и хранится {self.home.table_with_money} денег."
        
    def eat(self):
        energy, food = 10, 10
        if self.home.fridge >= food:
            self.lvl_hunger += energy
            self.home.human_eat(food)
            return f"{self.name} поел.\nУ него прибавилось {energy} энергии.\nТеперь его степень сытости равна {self.lvl_hunger}.\n\
Еды в холодильнике осталось {self.home.fridge}"
        else:
            return f"В доме недостаточно еды!"
            
    def job(self):
        energy, money = 10, 50
        
        self.lvl_hunger -= energy
        self.home.add_money(money)
        return f"{self.name} сегодня поработал!\nОн заработал {money}.\nПри этом он устал и потерял {energy} энергии.\n\
Чувство сытости {self.name} равна {self.lvl_hunger}.\nКоличество денег в доме составляет {self.home.table_with_money}."
        
        
    def play(self):
        energy = 5           
        self.lvl_hunger -= energy
        return f"{self.name} поиграл от души и потерял {energy}.\nЧувство сытости {self.name} равна {self.lvl_hunger}."
        
        
    def go_to_magazine(self):
        food, money = 15, 50
        if self.home.table_with_money >= 50:
            self.home.human_add_fridge(food)
            self.home.spend_money(money)
            return f"{self.name} сходил в магазин и купил {food} еды.\nПри этом денег в доме уменьшилось на {money}.\n\
Еды в холодильнике осталось {self.home.fridge}.\nКоличество денег в доме составляет {self.home.table_with_money}."
        else:
            return "У меня не хватает денег, чтобы купить себе еды!"
        
    def live_one_day(self):
        ch = rnd(1, 6)
        if self.lvl_hunger <= 20:
            print(self.eat())
        elif self.home.fridge <= 10:
            print(self.go_to_magazine())
            if self.home.table_with_money < 50:
                print(self.job())
        elif ch == 1:
            print(self.job())
        elif ch == 2:
            print(self.eat())
        else:
            print(self.play())
        # self.lvl_hunger -= 5

        
class Home:
    def __init__(self) -> None:
        self.fridge = 50 # холодильник
        self.table_with_money = 0
        
    def human_eat(self, food):
        self.fridge -= food
        
    def human_add_fridge(self, food):
        self.fridge += food
        
    def add_money(self, money):
        self.table_with_money += money
        
    def spend_money(self, money):
        self.table_with_money -= money
        

def live_day(human):
    return 1 if human.lvl_hunger <= 0 else 0


if __name__ == "__main__":
    home = Home()
    man = Human("Василий", home)
    women = Human("Юля", home)
    for i in range(1,366):
        man.live_one_day()
        women.live_one_day()
        print(f"{man.name} и {women.name} прожил {i} день.")
        if live_day(man) or live_day(women):
            print(f"{man.name} умер на {i} день своего существования.")
            print(man)
            break
        print()
        print("=" * 20)
        print("=" * 20)
        print()
    else:
        print(man)