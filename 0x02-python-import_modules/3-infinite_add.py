#!/usr/bin/python3

import sys
if __name__ == "__main__":
    sum = 0
    for arg in sys.argv:
        sum += int(arg)
    print(sum)
