#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list with replaced elements using list comprehension
    return [replace if x == search else x for x in my_list]
