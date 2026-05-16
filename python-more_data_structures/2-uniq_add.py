#!/usr/bin/python3
def uniq_add(my_list=[]):
    # set(my_list) removes all duplicates, sum() adds the remaining unique numbers
    return sum(set(my_list))
