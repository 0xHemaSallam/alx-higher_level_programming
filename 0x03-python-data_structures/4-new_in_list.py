#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length_list = len(my_list) - 1
    if idx < 0 or idx > length_list:
        return my_list.copy()
    else:
        new_my_list = my_list.copy()
        new_my_list[idx] = element
        return new_my_list
