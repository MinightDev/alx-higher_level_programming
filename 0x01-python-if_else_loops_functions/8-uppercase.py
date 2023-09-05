#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        result += chr(char_code)
    print(result)
