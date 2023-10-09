#!/usr/bin/python3
"""
Contains the MyList class
"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
