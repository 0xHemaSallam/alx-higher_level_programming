#!/usr/bin/python3

def no_c(my_string):
    
    result_list = []

    for char in my_string:

        if char != 'c' and char != 'C':
            result_list.append(char)

    result = ''.join(result_list)

    return result