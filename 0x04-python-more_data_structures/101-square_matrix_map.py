#!/usr/bin/python3
def square_matrix_map(matrix=[[]]):
    def helper_map(mylist):
        return list(map(lambda x: x**2, mylist))
    return list(map(helper_map, matrix))
