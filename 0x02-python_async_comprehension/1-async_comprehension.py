#!/usr/bin/env python3
'''a module ith asyn await'''
import asyncio
import random
from typing import Generator, List
async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''async comprehensions'''
    return [random async for random in async_gen()]
