#!/usr/bin/env python3
"""
This module contains an abstract base class Shape, its concrete subclasses
Circle and Rectangle, and a utility function shape_info designed
to demonstrate duck typing in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class that serves as an interface for geometric shapes."""

    @abstractmethod
    def area(self):
        """Compute the area of a shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of a shape."""
        pass


class Circle(Shape):
    """Concrete implementation of Shape representing a circle."""

    def __init__(self, radius):
        """Initialize a Circle instance with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete implementation of Shape representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")