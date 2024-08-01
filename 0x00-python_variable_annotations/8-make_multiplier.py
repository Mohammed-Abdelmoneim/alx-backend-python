#!/usr/bin/env python3
"""Type-annotated function make_multiplier."""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns fucntion."""
    def mul(a: float) -> float:
        return float(a * multiplier)
    return mul
