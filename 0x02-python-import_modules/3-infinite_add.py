#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    ln = len(argv)

    for x in range(1, ln):
        sum += int(argv[x])
    print("{:d}".format(sum))
