#!/usr/bin/python3


"""Mudule that prints a square"""


def print_square(size):
    """Function that prints a square"""

    if size == 0:
        print()

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
