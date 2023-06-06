#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if ord(x) in range(97, 123):
            num = 32
        else:
            num = 0
        print("{}".format(chr(ord(x) - num)), end='')
    print('')
