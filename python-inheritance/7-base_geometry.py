#!/usr/bin/python3
"""
Defines a BaseGeometry class with input verification.
"""


class BaseGeometry:
    """
    A foundational class handling shape logic and data integrity.
    """

    def area(self):
        """
        Calculates area, currently not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the parameter value is a strictly positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
