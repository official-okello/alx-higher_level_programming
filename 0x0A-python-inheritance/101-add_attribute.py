#!/usr/bin/python3
""" Main container """


def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
