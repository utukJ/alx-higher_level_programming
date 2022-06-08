#!/usr/bin/python3

def only_diff_elements(set1, set2):
    intersect = set1.intersection(set2)
    union = set1.union(set2)
    return union.difference(intersect)
