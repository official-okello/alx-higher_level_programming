#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
if len(sys.argv) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
else:
    op = sys.argv[1]
    a = sys.argv[0]
    b = sys.argv[2]

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
