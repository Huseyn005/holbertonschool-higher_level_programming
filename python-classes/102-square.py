#!/usr/bin/python3
"""
This module defines a class Square with rich comparison capabilities.
"""


class Square:
    """
    Defines a square by size, handles type/value validation, area calculation,
    and supports comparison operators based on area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int/float): The size of the square's sides. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int/float: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int/float): The new size value to set.

        Raises:
            TypeError: If value is not an int or a float.
            ValueError: If value is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int/float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Handles the == comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Handles the != comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Handles the < comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Handles the <= comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Handles the > comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Handles the >= comparison based on area."""
        return self.area() >= other.area()
