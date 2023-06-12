#!/usr/bin/python3

def max_integer(my_list=[]):
    x = len(my_list)
    if x < 1:
        return (None)

    max = my_list[0]
    for i in range(1, x):
        if my_list[i] > max:
            max = my_list[i]
    return (max)
