#!/usr/bin/python3

def remove_char_at(str, n):
    for x in range(len(str)):
        if n > len(str):
            print(str)
        else:
            if str[x] == str[n]:
                print('', end='')
            else:
                print(str[x], end='')
