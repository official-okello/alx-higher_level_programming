#!/usr/bin/python3

for x in range(100):
    if x % 10 > x / 10:
        if x != 89:
            print("{:02d}".format(x), end=', ')
        else:
            print(x)
