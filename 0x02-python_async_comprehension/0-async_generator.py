#!/usr/bin/env python3
'''Async Generator
'''
import asyncio
import random
from typing import Generator
# Generator[yield_type, send_type, return_type]

async def async_generator() -> Generator[float, None, None]:
    '''Coroutine that generates a sequence of 5 numbers.
    '''
    for _ in range(5):
        await asyncio.sleep(1)
        yield random.random() * 5
