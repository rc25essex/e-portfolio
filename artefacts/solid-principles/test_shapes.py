from shapes import Circle, Square, Triangle
import math


def test_circle_area():
    circle = Circle(25)
    assert circle.calculate_area() == math.pi * 625


def test_square_area():
    square = Square(10)
    assert square.calculate_area() == 100


def test_triangle_area():
    triangle = Triangle(5, 2)
    assert triangle.calculate_area() == 5
