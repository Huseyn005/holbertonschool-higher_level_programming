#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate through the sorted list of first-level keys
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
