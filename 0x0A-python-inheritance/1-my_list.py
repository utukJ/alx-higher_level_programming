#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """Extends list to implement printing sorted"""

    def print_sorted(self):
        print(sorted(self))
