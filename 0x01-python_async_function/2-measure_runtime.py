#!/usr/bin/env python3
""" Measure the runtime"""
from timeit import default_timer as timer
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)."""
    start = timer()
    asyncio.run(wait_n(n, max_delay))
    end = timer()
    t = end - start
    return t / n
