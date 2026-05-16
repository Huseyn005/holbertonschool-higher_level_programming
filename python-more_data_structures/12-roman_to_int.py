#!/usr/bin/python3
def roman_to_int(roman_string):
    # Handle edge cases: must be a non-empty string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # Define standard Roman numeral values
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)
    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)
        # If the current numeral is smaller
        # than the next one, subtract it
        if i + 1 < length \
        and current_val < roman_dict.get(roman_string[i + 1], 0):
            total -= current_val
        else:
            total += current_val
    return total
