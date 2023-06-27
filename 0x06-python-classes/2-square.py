#!/usr/bin/python3
class Square:
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
