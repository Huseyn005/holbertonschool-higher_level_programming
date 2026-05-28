#!/usr/bin/python3
"""
Defines a polished Square class inheriting of Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents an equilateral rectangle object with custom print format.
    """

    def __init__(self, size):
        """
        Initializes structural attributes matching square logic rules.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a formatted representation string of the square object.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
