#!/usr/bin/python3
# Author - Udenyi Joshua
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
