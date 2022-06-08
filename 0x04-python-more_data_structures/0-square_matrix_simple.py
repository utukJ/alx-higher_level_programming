#!/usr/bin/python3

def square_matrix_simple(matrix=[[]]):
    new_mat = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col**2)
        new_mat.append(new_row)
    return new_mat
