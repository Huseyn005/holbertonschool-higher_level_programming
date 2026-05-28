#!/usr/bin/python3
"""
Defines a class MyList that derives of list.
"""


class MyList(list):
    """
    Implements a custom list with built-in printing capabilities.
    """

    def print_sorted(self):
        """
        Prints the elements of the collection sorted in ascending order.
        """
        print(sorted(self))
