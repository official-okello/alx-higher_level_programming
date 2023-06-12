#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    if x < 1:
        n_tuple = (x, "None")
    else:
        n_tuple = (x, sentence[0])
    return (n_tuple)
