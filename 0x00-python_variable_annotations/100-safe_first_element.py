#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a list input_list
    of anything and returns its first element"""

from typing import Union, Any, Sequence, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type-annotated function safe_first_element that takes a list input_list
    of anything and returns its first element"""
    if lst:
        return lst[0]
    else:
        return None
