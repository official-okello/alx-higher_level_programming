#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if ord(x) in range(97, 123):
            print("{:c}".format(ord(x - 32)), end='')
        else:
            print(x, end='')
