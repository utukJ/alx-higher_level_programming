#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dorime = []
    for k, v in a_dictionary.items():
        if v == value:
            dorime.append(k)
    for key in dorime:
        del a_dictionary[key] 
