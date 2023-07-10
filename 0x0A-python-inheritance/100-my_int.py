#!/usr/bin/python3
""" Main container """


class MyInt(int):
    """ Class that inherits from Class Int"""

    def __eq__(self, other):
        """ Method that returns != check """

        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """

        return int.__eq__(self, other)
