#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound"""
        pass


class Dog(Animal):
    """Subclass representing a dog"""

    def sound(self):
        """Returns the dog sound"""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat"""

    def sound(self):
        """Returns the cat sound"""
        return "Meow"
