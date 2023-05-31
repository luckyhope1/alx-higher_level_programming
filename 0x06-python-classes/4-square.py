#!/usr/bin/python3
"""A square class definition"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        """initializes size of self with size"""
        self.__size = size

    @property
    def size(self):
        """returns __size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """"""
        if not isinstance(value, int):
            """"""
            raise TypeError("size must be an integer")
        if value < 0:
            """"""
            raise ValueError("size must be >= 0")
        self.__size = value
        """defines area function"""
    def area(self):
        """returns area"""
        return self.__size ** 2
