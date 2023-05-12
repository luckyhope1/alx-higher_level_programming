#!/usr/bin/python3
for j in range(0, 90):
    if j % 10 > j / 10:
        if j != 89:
            print("{:02d}, ".format(j), end='')
        else:
            print("{:02d}".format(j))
