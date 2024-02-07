#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictB = dict(a_dictionary)
    for idx, item in dictB.items():
        if item == value:
            del a_dictionary[idx]
    return a_dictionary
