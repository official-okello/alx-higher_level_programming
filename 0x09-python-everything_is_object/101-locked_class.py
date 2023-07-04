#!/usr/bin/python3


"""Module that containts a class that avoids dynamically created attributes"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Initializes the class instance """
        pass
