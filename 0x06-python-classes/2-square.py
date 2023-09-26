#!/usr/bin/python3
"""This module defines a Square class."""
class Square:
    """Square class with private instance attribute: size."""

    def __init__(self, size=0):
        """Initialize the Square instance with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
