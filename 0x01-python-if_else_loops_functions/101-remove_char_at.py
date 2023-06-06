#!/usr/bin/python3

def remove_char_at(str, n):
    if n > len(str) or str == '':
        print(str)
	else:
        for x in range(len(str)):
            if str[x] == str[n]:
                print('', end='')
            else:
                print(str[x], end='')
