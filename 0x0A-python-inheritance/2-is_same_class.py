#!/usr/bin/python3
"""
Contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class

    Args:
        obj: The object to check
        a_class: The class to compare with

    Returns:
        True if obj is an instance of a_class, otherwise False
    """
    return type(obj) is a_class
