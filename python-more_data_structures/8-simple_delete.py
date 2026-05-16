#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Removes the key if it exists; returns None instead of failing if missing
    a_dictionary.pop(key, None)
    return a_dictionary
