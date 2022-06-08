#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    skeys = sorted(list(a_dictionary.keys()))
    for k in skeys:
        print("{k}: {a_dictionary[k]}")
