#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar_matrix = []

    for row in matrix:
        row = list(map(lambda x: x**2, row))
        squar_matrix.append(row)
    return (squar_matrix)
