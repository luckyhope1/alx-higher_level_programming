#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122: # ASCII code of lowercase letters
            # Convert lowercase letters to uppercase using ASCII code
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
