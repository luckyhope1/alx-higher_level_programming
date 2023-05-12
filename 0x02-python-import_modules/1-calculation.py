#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum_ab = add(a, b)
    diff_ab = sub(a, b)
    prod_ab = mul(a, b)
    quot_ab = div(a, b)
    print("The sum of", a, "and", b, "is", sum_ab)
    print("The difference between", a, "and", b, "is", diff_ab)
    print("The product of", a, "and", b, "is", prod_ab)
    print("The quotient of", a, "and", b, "is", quot_ab)
