#!/usr/bin/python3
"""
Defines a fully implemented Rectangle class inheriting of BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a standard operational geometric rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the instance parameters securely.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area evaluation of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a formatted representation string of the object.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
