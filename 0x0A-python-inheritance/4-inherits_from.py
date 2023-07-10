#!/usr/bin/python3
""" Main container """


def inherits_from(obj, a_class):
    """ Defines the class """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
