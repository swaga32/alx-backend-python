#!/usr/bin/env python3
'''Task 4
'''
import asyncio
import time
from importlib import import_module as find


async_comprehension = find('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
