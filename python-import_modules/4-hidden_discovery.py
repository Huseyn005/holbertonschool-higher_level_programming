#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the hidden_4 module
    names = dir(hidden_4)
    
    # Filter out names that start with "__" and print them
    for name in names:
        if not name.startswith("__"):
            print("{}".format(name))
