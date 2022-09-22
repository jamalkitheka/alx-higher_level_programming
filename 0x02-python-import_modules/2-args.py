#!/usr/bin/python3
from sys import argv

def arguments():
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            arg = 'argument:'
        else:
            arg = 'arguments:'
        print("{} {}".format(len(argv) - 1, arg))
        for x in range(1, len(argv)):
            print("{}: {}".format(x, argv[x]))

if __name__ == "__main__":
    arguments()
