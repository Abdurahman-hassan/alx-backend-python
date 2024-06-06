#!/usr/bin/env python3
"""Type-annotated function element_length that
    takes a list input_list of string as argument and returns a list"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
