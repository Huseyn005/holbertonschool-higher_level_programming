#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0

    # Skip the first element (script name) and loop through the rest
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
