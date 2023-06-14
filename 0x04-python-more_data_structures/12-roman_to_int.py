#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if type(roman_string) is not str:
        return (0)
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = len(roman_string)
    value_int = romans[roman_string[number-1]]
    for i in range(number-1, 0, -1):
        current = romans[roman_string[i]]
        prev = romans[roman_string[i-1]]
        if prev >= current:
            value_int += prev
        else:
            value_int -= prev
    return (value_int)
