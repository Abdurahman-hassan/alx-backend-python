#!/usr/bin/env python3
"""Type-annotated function element_length that
    takes a list input_list of string
    as argument and returns a list"""
from typing import List


def element_length(lst: List[str]) -> List[int]:
    """Return a list of integers representing
        the lengths of the strings in lst"""
    return [len(x) for x in lst]
