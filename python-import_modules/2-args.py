#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Count excludes the script name itself
    count = len(sys.argv) - 1

    # Determine the correct punctuation and pluralization
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Print each argument with its corresponding 1-indexed position
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
