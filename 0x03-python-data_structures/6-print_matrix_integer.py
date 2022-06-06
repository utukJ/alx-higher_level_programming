#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(("{:d} "*len(row))[:-1].format(*row))
