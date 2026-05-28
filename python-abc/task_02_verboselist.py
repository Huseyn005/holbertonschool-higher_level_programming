#!/usr/bin/env python3
"""
Module containing the VerboseList class that extends the built-in list
to provide notifications when items are added or removed.
"""


class VerboseList(list):
    """A custom list that prints notifications on modifications."""

    def append(self, item):
        """Adds an item to the end of the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with items from an iterable and prints a notification."""
        # Convert to a list or check length before extending to know how many items are added
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Removes the first occurrence of an item and prints a notification."""
        # Note: If the item isn't in the list, super().remove will raise a ValueError.
        # We print the message right before removing, as requested.
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns an item at the given index (default last item)."""
        # Retrieve the item first so we can print it before it gets popped
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
