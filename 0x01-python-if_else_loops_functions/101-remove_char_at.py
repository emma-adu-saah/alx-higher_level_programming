#!/usr/bin/python3
def remove_char_at(str, n):
    string_list = list(str)
    new_str = ""
    if n < 0 or n > len(str):
        return str
    string_list[n] = ""
    for i in string_list:
        new_str += i
    return new_str
