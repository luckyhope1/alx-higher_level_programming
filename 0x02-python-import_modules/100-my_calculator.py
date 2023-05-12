#!/usr/bin/env python3
import sys
from calculator_1 import *

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, res))
