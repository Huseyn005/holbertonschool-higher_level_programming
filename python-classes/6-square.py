#!/usr/bin/python3
"""
This module defines a class Square with size and position properties.
"""


class Square:
    """
    Defines a square by its size and coordinate position, handles validation,
    area calculation, and custom printing with offsets.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square's sides. Defaults to 0.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position coordinates of the square.

        Returns:
            tuple: A tuple of two non-negative integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position coordinates of the square with type/value validation.

        Args:
            value (tuple): The position coordinates (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character to stdout, incorporating
        the horizontal and vertical offsets defined by position.
        """
        if self.__size == 0:
            print()
            return

        # Print the vertical space (y coordinate)
        for _ in range(self.__position[1]):
            print()

        # Print the square body with horizontal space (x coordinate)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
