#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)
    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)
        # Slicing safely handles out-of-bounds index by returning empty string
        next_char = roman_string[i + 1:i + 2]
        next_val = roman_dict.get(next_char, 0)
        if current_val < next_val:
            total -= current_val
        else:
            total += current_val
    return total
