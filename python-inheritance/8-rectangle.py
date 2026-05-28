#!/usr/bin/python3
"""
Defines a Rectangle class inheriting of BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using parameters verified by BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with private attributes.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
