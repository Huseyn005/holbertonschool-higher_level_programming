def uppercase(str):
    for char in str:
        # Check if the character is lowercase using ASCII values
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("{}".format(""))
