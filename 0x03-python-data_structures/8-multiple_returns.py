#!/usr/bin/python3

def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        return n, None
    return n, sentence[0]
