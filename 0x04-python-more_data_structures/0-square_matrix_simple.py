#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for i in range(len(matrix)):
        n_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (n_matrix)
