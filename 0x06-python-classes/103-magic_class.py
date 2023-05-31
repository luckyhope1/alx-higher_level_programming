#!/usr/bin/python3
""" declares a class called MagicClass """
import math


class MagicClass:
    """definition of methods area and circumference"""
    def __init__(self, radius):
        """The __init__ method initializes a MagicClass instance with a given radius."""
        self.__radius = 0

        """Type checking for the radius parameter"""
        if type(radius) is not int and type(radius) is not float:
            """Raise a TypeError if the radius is not a number."""
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of a circle with radius self.__radius."""
        return 2 ** self.__radius * math.pi

    def circumference(self):
        """Calculates and returns the circumference of a circle with radius self.__radius."""
        return 2 * math.pi * self.__radius
