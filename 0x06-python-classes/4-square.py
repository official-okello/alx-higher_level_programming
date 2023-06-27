#!/usr/bin/python3
""" Square Class """


class Square:
    """ Declares a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Gets attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets attribute """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes area of a square """
        return (self.__size ** 2)
