#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is valid and not empty
    if not a_dictionary:
        return None
    # Find and return the key with the maximum value
    return max(a_dictionary, key=a_dictionary.get)
