#!/usr/bin/env python3
"""
Module demonstrating the use of Mixins in Python.
Provides SwimMixin, FlyMixin, and a Dragon class that utilizes both.
"""


class SwimMixin:
    """A mixin that provides swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that composes behaviors from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints a roaring message distinct to the dragon."""
        print("The dragon roars!")
