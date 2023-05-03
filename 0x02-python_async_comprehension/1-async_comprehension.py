#!/usr/bin/env python3
'''Task 8
'''
from typing import List
from importlib import import_module as find

async_generator = find('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    random_nums = [num async for num in async_generator()]
    return random_nums[:10]
