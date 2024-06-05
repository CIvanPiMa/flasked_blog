"""
This module contains utility functions and classes that are used across the application.
"""

from typing import Type, TypeVar, Dict

T = TypeVar("T")


class SingletonMeta(type):
    """
    A metaclass that ensures that only one instance of a class is created and shared across the application.
    """
    _instances: Dict[Type[T], T] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
