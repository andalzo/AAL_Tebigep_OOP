import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


def print_shape_info(shape: Shape):
    data = {
        "name": shape.__class__.__name__,
        "area": shape.calculate_area(),
        "perimeter": shape.calculate_perimeter(),
    }
    print(data)


if __name__ == '__main__':
    shapes = [
        Rectangle(10, 15),
        Square(8),
        Circle(12),
    ]

    for shape in shapes:
        print_shape_info(shape)
