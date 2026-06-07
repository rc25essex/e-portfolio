from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 2)

print("Circle area:", circle.calculate_area(), "m²")
print("Square area:", square.calculate_area(), "m²")
print("Triangle area:", triangle.calculate_area(), "m²")

shapes = [Circle(7), Square(10), Triangle(5, 3)]

for shape in shapes:
    print(type(shape).__name__, "area:", shape.calculate_area(), "m²")
