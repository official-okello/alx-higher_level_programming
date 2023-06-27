#!/usr/bin/python3
class Square:
    '''Defines a square by its size
    '''
    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    '''Defines a Square class
    '''
    def __init__(self, size=0):
        '''Initializes the Square class with valid size attribute.
        '''
        try:
            self.__size = int(size)
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        except Exception:
            raise TypeError("size must be an integer")

    def area(self):
        '''Returns the area of the square
        '''
        return (self.size ** 2)

    @property
    def size(self):
        '''Returns the size value
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size value of the square object
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
