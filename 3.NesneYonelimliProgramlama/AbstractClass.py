from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def voice(self):
        pass


class Bird(Animal):

    def voice(self):
        print("Bird: Tweet")


class Dog(Animal):

    def voice(self):
        print("Dog: Woof")


class Cat(Animal):

    def voice(self):
        print("Cat: Meow")


class Zoo:

    def __init__(self):
        self.animals: list[Animal] = list()

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def voice_all(self):
        for animal in self.animals:
            animal.voice()


def main():
    bird = Bird()
    dog = Dog()
    cat = Cat()

    zoo = Zoo()
    zoo.add_animal(bird)
    zoo.add_animal(dog)
    zoo.add_animal(cat)

    zoo.voice_all()


if __name__ == "__main__":
    main()
