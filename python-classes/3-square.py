#!/usr/bin/python3
"""
This module defines a class Square with validation and an area method.
"""


class Square:
    """
    Defines a square by its size and calculates its area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
