#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints integers in list"""
    for i in my_list[::-1]:
        print(f"{i:d}")


if __name__ == "__main__":
    my_list = [1]
    print_reversed_list_integer(my_list)
