#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for a in range(0, len(arr)):
        if arr[a][0:2] != "__":
            print("{}".format(arr[a]))
