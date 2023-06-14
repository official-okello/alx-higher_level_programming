#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_mat = matrix.copy()
    for i in matrix:
        n_mat.append(list(map((lambda x: x ** 2), i)))
    return (n_mat)
