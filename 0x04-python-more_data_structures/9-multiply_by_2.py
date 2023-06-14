#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = {}

    for i in a_dictionary:
        n_dict.update({i: a_dictionary[i]*2})
    return (n_dict)
