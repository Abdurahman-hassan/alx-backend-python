#!/usr/bin/env python3
"""task 9 module"""
from typing import List


def element_length(lst: List[str]) -> List[int]:
    """Return a list of integers representing
        the lengths of the strings in lst"""
    return [len(x) for x in lst]
