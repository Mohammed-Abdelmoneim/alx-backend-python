#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random"""
    delay: float = random.uniform(0, max_delay)
    return delay
