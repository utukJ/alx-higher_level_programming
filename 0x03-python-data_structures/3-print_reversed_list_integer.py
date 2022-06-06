#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints integers in list"""
    for i in my_list[::-1]:
        print("{:d}".format(i))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    print_reversed_list_integer(my_list)
    print("--")
    print_reversed_list_integer([0, 1, 8])
