#!/usr/bin/python3
"""Contains BaseGeometry class"""

class BaseGeometry:
    """Basic geometry operations"""
    def area(self):
        """Raises Exception: area() not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer. TypeError: not int. ValueError: <= 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

