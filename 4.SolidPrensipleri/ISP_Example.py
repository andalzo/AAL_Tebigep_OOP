from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Fliable:
    @abstractmethod
    def fly(self):
        pass


class Cat(Animal):
    def eat(self):
        return True

    def walk(self):
        return True


class Duck(Animal, Swimmable):
    def eat(self):
        return True

    def walk(self):
        return True

    def swim(self):
        return True


class Pigeon(Animal, Fliable):
    def eat(self):
        return True

    def walk(self):
        return True

    def fly(self):
        return True
