#!/usr/bin/env python3
"""Type-annotated function to_kv."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    t = (k, v ** 2)
    return t
