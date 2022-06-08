#!/usr/bin/python3

def best_score(a_dictionary):
    biggest_key, biggest_val = None, None
    for key, val in a_dictionary.items():
        if biggest_key is None or val > biggest_val:
            biggest_key, biggest_val = key, val
    return biggest_key
