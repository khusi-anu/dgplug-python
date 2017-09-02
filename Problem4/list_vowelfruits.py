#!/usr/bin/env python3

basket = ["apple", "banana", "pineapple", "mango"]
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print("The fruits whose names start with a vowel are: ")

serial_number = 0
for fruits in basket:
    if fruits[0] in vowel:
        serial_number = serial_number + 1
        print(serial_number, ".", fruits)
