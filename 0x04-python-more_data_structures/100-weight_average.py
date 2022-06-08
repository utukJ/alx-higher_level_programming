#!/usr/bin/python3
def weight_average(my_list=[]):
    total, div = 0, 0
    if len(my_list) == 0:
        return 0
    for score, weight in my_list:
        total += score * weight
        div += weight
    return total / div
