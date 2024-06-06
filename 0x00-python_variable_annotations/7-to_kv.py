#!/usr/bin/env python3
"""
Annotate the below function’s parameters
    and return values with the appropriate types
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string
        and the square of the number
    """
    return (k, pow(v, 2))
