#!/usr/bin/python3
"""
This module defines classes for a singly linked list data structure.
"""


class Node:
    """
    Defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Args:
            data (int): The data value stored inside the node.
            next_node (Node): The next node in the chain. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node with type validation.

        Args:
            value (int): The integer value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node reference.

        Returns:
            Node: The next connected Node object or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node reference with type validation.

        Args:
            value (Node): The next Node object or None.

        Raises:
            TypeError: If value is neither None nor a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list structure.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list with a hidden head reference.
        """
        self.__head = None

    def __str__(self):
        """
        Defines the printable representation of the linked list.

        Returns:
            str: One node data number per text line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value to insert as a new node.
        """
        new_node = Node(value)

        # Case 1: The list is completely empty, or value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Traverse to find the insertion point in the middle or at the end
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        # Insert the new node behind the matched boundary node
        new_node.next_node = current.next_node
        current.next_node = new_node
