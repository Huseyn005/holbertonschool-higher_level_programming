#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList class."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Instantiate a Node with data and an optional next_node.

        Args:
            data (int): The data stored in the node.
            next_node (Node or None): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with type validation.

        Args:
            value (int): The data value to store.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with type validation.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with sorted insertion."""

    def __init__(self):
        """Instantiate an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Return a string of each node's data on its own line."""
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)

    def sorted_insert(self, value):
        """Insert a new Node in the correct sorted position (ascending order).

        Args:
            value (int): The data value for the new node.
        """
        new_node = Node(value)

        # Insert at head if list is empty or value is smallest
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse to find the correct insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert between current and current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node