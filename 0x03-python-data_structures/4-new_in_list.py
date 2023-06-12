#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        new_list = my_list
        return (new_list)
    else:
        my_list[idx] = element
        return (my_list)
