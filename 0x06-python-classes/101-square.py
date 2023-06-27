#!/usr/bin/python3
class Square:
    '''Defines a square by its size
    '''
    def __str__(self):
        rtn = ""

        if self.size == 0:
            return rtn

        for i in range(self.position[1]):
            rtn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rtn += " "
            for j in range(self.size):
                rtn += "#"
            if i is not (self.size - 1):
                rtn += "\n"

        return rtn

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

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''Prints the square initialized above
        '''
        for i in range(self.position[1]):
            print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
