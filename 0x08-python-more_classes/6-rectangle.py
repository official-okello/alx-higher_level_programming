#!/usr/bin/python3


"""Defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method that returns the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method that returns the perimeter of a rectangle"""
        if self.heigth == 0 and self.width == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """Method that returns the Rectangle with #"""
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Method that returns the string represantion of the instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
