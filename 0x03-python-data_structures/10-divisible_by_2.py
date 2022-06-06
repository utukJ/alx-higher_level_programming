#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    mask = [True if k % 2 == 0 else False for k in my_list]
    return mask
