#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    for name in dir(hidden_4):
        if name[:1] != '__':
            print(name)
