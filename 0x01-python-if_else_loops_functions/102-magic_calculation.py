#!/usr/bin/python3
import dis

def magic_calculation(a, b, c):
    if b < a:
        return c
    elif b > c:
        return a + b
    else:
        return a * b - c

dis.dis(magic_calculation)
