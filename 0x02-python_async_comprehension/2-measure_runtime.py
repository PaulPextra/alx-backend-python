#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run time for four parallel comprehensions
    """

    start = perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*tasks)
    end = perf_counter() - start
    return end
