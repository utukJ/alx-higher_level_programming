#!/usr/bin/python3

def element_at(my_list, idx):
    """returns element at index idx in my_list"""
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(element_at(my_list, 3))
