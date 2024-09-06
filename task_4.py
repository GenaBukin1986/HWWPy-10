import abc
class Animal(abc.ABC):
    def __init__(self, name: str):
        self.name = name
    @abc.abstractmethod
    def speak(self):
        pass


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan  # размах крыльев

    def wing_length(self):
        return f"Длина крыла {self.wingspan / 2} {self.name}"

    def speak(self):
        return f"Ku-ka-re-ku"


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth  # максимальная глубина обитания

    def depth(self):
        """метод, который возвращает категорию глубины рыбы
           (мелководная, средневодная, глубоководная) в
           зависимости от значения max_depth"""
        result = "Средневодная рыба"
        if self.max_depth < 10:
            result = "Мелководная рыба"
        elif self.max_depth > 100:
            result = "Глубоководная рыба"
        return f"{self.name} {result}"

    def speak(self):
        return 'Am-am'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight  # вес

    def category(self):
        """метод, который возвращает категорию млекопитающего
        в зависимости от веса."""
        result = "Обычный"
        if self.weight < 1:
            result = "Малявка"
        elif self.weight > 200:
            result = "Гигант"
        return f"{self.name} относится к категории {result}"

    def speak(self):
        return "rrrrrrrrrrr!"


class AnimalFactory:
    def __init__(self, animal: Animal, *args):
        self.animal = animal
        self.name = args[0]
        self.params = args[1]

    def create_animal(self):
        match self.animal:
            case 'Bird':
                return Bird(self.name, self.params)
            case 'Fish':
                return Fish(self.name, self.params)
            case 'Mammal':
                return Mammal(self.name, self.params)
            case _:
                raise ValueError('Недопустимый тип животного')


if __name__ == '__main__':
    bird = AnimalFactory("Bird", 'Flippy', 5).create_animal()
    fish = AnimalFactory('Fish', "Guppy", 59).create_animal()
    manall = AnimalFactory('Mammal', "Barry", 1).create_animal()
    for animal in [bird,fish,manall]:
        if isinstance(animal, Bird):
            print(animal.wing_length())
        elif isinstance(animal, Fish):
            print(animal.depth())
        else:
            print(animal.category())
        print(animal.speak())
    # dog = AnimalFactory("Dog","Bob", 56).create_animal() # ValueError: Недопустимый тип животного