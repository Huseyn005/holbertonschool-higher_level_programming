#!/usr/bin/python3
"""
Defines a basic Square class inheriting of Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents an equilateral rectangle object.
    """

    def __init__(self, size):
        """
        Initializes structural attributes matching square logic rules.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
