#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square with a private instance attribute 'size'."""

    def __init__(self, size=0):
        """Initializes a square instance with an optional size."""
        self.size = size

    @property
    def size(self):
        """Getter for __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
