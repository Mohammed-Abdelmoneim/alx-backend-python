#!/usr/bin/env python3
from typing import List
"""Type-annotated function sum_list."""


def sum_list(input_list: List[float]) -> float:
    """Returns the sum as a float."""
    sum: float = 0
    for l in input_list:
        sum += l
    return sum
