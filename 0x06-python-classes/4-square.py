#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """Getter for __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size
        Args:
            value (int): The size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2
