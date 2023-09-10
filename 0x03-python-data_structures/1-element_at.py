#!/usr/bin/python3
def element_at(my_list, i):
    if i < 0 or i >= len(my_list):
        raise IndexError("Index out of bounds")
    return my_list[i]
