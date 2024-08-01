#!/usr/bin/env python3
"""Type-annotated function element_length."""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list."""
    return [(i, len(i)) for i in lst]
