#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_mat = matrix.copy()
    for i in matrix:
        new_matrix.append(list(map((lambda x: x ** 2), i)))
    return new_matrix
