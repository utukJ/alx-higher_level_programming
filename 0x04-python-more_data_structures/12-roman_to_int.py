#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0

    result = 0

    conv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i, ch in enumerate(roman_string):
        if i < len(roman_string) - 1 and conv[ch] < conv[roman_string[i+1]]:
            result -= conv[ch]
        else:
            result += conv[ch]
    return result
