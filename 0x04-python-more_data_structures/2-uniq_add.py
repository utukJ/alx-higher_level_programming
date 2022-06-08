#!/usr/bin/python3

def uniq_add(mylist=[]):
    memo = dict()
    result = 0
    for num in mylist:
        if num not in memo:
            result += num
            memo[num] = 1
    return result
