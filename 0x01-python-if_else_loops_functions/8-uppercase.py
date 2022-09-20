#!/usr/bin/python3
def uppercase(string):
    result = ''
    for i in range(0, len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            result += chr(ord(string[i]) - 32)
        else:
            result += string[i]
    print("{:s}".format(result))
