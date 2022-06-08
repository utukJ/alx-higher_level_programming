#!/usr/bin/python3

def search_replace(mylist, search, replace):
    return list(map(lambda x: replace if x == search else x, mylist))
