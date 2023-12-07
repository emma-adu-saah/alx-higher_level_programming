#!/usr/bin/python3
def uppercase(str):
    final_str = ""
    for string in str:
        string_ascii = ord(string)
        if string_ascii >= 97 and string_ascii <= 122:
            letter = string_ascii - 32
            final_str = final_str + chr(letter)
        else:
            final_str = final_str + chr(string_ascii)
    print("{}".format(final_str))


    
