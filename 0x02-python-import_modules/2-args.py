#!/usr/bin/python3

import sys
if __name__ == "__main__":
    length = len(sys.argv)

    if i == 1:
        print("{} arguments.".format(length))
    elif i == 2:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))

    for i in range(1, length):
        print('{:d}: {:s}'.format(i, sys.argv[i]))
