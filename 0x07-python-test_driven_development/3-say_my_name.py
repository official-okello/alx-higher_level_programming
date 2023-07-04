#!/usr/bin/python3


"""Module that prints my name"""


def say_my_name(first_name, last_name=""):
    """Function that prints my name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
