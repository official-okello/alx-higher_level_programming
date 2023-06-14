#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_mat = matrix.copy()

    for i in range(len(matrix)):
    n_mat[i] = list(map(lambda x: x **2, matrix[i]))
    return (n_mat)
