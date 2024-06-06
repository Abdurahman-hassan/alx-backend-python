#!/usr/bin/env python3
"""
Annotate the below function’s parameters
    and return values with the appropriate types
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats
    """
    return sum(mxd_lst)
