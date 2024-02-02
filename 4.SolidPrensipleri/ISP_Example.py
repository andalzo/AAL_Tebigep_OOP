from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Cat(Animal):
    def eat(self):
        return True

    def walk(self):
        return True

    def swim(self):
        raise NotImplemented

    def fly(self):
        raise NotImplemented


class Duck(Animal):
    def eat(self):
        return True

    def walk(self):
        return True

    def swim(self):
        return True

    def fly(self):
        raise NotImplemented


class Pigeon(Animal):
    def eat(self):
        return True

    def walk(self):
        return True

    def swim(self):
        raise NotImplemented

    def fly(self):
        return True
