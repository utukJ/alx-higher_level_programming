#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces element at index idx in my_list"""
    my_list_copy = my_list[:]
    if 0 <= idx < len(my_list_copy):
        my_list_copy[idx] = element
    return my_list_copy


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(replace_in_list(my_list, 3, 11))
