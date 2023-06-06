#!/usr/bin/python3

def remove_char_at(str, n):
    for x in str:
        if str[n] == x:
            print('')
        else:
            print(x, end='')
