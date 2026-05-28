#!/usr/bin/python3
"""
Defines a subclass verification function.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is a subclass instance (direct or indirect).
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
