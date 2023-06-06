#!/usr/bin/python3

def remove_char_at(str, n):
    for x in str:
        if x == str[n]:
            print('', end='')
        else:
            print(x, end='')
