#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None
    return (result)
