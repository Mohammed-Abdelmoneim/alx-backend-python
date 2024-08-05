#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Wait random"""
    delay = random.uniform(0, max_delay)
    return delay
