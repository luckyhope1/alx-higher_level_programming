#!/usr/bin/python3
""" declaration of  a class named Square """


class Square:
    def __init__(self, size=0):
        """ Check if size is an integer """
        if type(size) != int:
            raise TypeError("size must be an integer")
        
        """ Check if size is non-negative """
        if size < 0:
            raise ValueError("size must be >= 0")
        
        """ Assign the size to the private attribute __size """
        self.__size = size
