#!/usr/bin/env python3
"""asynchronous coroutine."""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """Waits for a random delay between 0 and max_delay."""
    i = 0
    ls = []
    while(i < n):
        res = await wait_random(max_delay)
        ls.append(res)
        i = i + 1
    return ls
