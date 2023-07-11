#!/usr/bin/python3
""" Module for pascal_triangle method """


def pascal_triangle(n):
    """ Returns a list of lists of integers """

    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
