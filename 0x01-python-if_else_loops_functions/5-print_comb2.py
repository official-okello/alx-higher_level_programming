#!/usr/bin/python3

for x in range(100):
    if x == 99:
        print(x)
    else:
        print("{:02d}".format(x), end=', ')
