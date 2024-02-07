#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    if len(my_list) > 0:
        total = 0
        denom = 0
        d = dict(my_list)
        for idx, item in d.items():
            total += int(idx) * int(item)
            denom += int(item)
        result = total / denom

    return (result)
