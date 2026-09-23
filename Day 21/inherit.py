class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.no_of_legs = 4

    def bark(self):
        print("woof woof")

dog = Dog()
dog.bark()
dog.breathe()
animal1 = Animal()
animal1.breathe()

