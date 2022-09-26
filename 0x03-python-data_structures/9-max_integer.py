#!/usr/bin/python3

def max_integer(my_list=[]):
    maximum = 0
    if not my_list:
        return("None")
    for x in range(len(my_list)):
        if my_list[x] > maximum:
            maximum = my_list[x]
    return(maximum)
