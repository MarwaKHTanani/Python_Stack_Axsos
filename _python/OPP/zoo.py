class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 50
        self.happiness = 50

    def display_info(self):
        print(f"Name: {self.name} ,health:{self.health} ,happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feed(self):
        self.health += 20
        self.happiness += 20


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feed(self):
        self.happiness += 15
        self.health += 25


class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feed(self):
        self.happiness += 17
        self.health += 5


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()
        return self


lion = Lion("Nala", 20)
lion.feed()

bear = Bear("Shere Khan", 70)
bear.feed()

monkey = Monkey("Rajah", 40)
monkey.feed()

zoo1 = Zoo("John's Zoo")
zoo1.add_animal(lion).add_animal(Lion("Simba", 17)).add_animal(monkey).add_animal(
    bear
).print_all_info()
