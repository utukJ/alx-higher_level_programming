#!/usr/bin/python3
"""This module implements a node class for singly linked list"""


class Node:
    """defines node for singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        tmp = self.__head
        prev = None
        while tmp is not None:
            if tmp.data >= value:
                if prev is None:
                    self.__head = Node(value, next_node=tmp)
                else:
                    new = Node(value, next_node=tmp)
                    prev.next_node = new
                return
            tmp, prev = tmp.next_node, tmp
        prev.next_node = Node(value)

    def __str__(self):
        result = ""
        tmp = self.__head
        while tmp is not None:
            result += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return result[:-1]
