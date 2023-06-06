#!/usr/bin/python3

def remove_char_at(str, n):
    for x in len(str):
        if n > len(str):
            pass
        else:
            if str[x] == str[n]:
                print('', end='')
            else:
                print(str[x], end='')
