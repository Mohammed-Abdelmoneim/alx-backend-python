#!/usr/bin/env python3
"""Type-annotated function element_length."""
from typing import List, Union, Tuple, Callable, Iterator, Sequence


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
