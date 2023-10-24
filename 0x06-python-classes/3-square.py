#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Instatiation of size """
    def __init__(self, size=0):
        """ size (int) the size of the new square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return the area of the Square. """
        return (self.__size * self.__size)
