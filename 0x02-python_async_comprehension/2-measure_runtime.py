#!/usr/bin/env python3
'''a module ith asyn await'''
import asyncio
import random
import time
from typing import Generator, List
a_cp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure time'''
    start = time.perf_counter()
    await asyncio.gather(a_cp(), a_cp(), a_cp(), a_cp())
    return time.perf_counter() - start
