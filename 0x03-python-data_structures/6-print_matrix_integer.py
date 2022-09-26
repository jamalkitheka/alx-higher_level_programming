#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
         print ('  '.join(map(str, sub_list)))
