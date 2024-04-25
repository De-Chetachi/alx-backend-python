#!/usr/bin/env python3
'''a module'''
import asyncio
import random
from typing import Union, List
wait_r = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''hmm oku'''
    delays = asyncio.run(wait_n(n, max_delay))
    sum_ = 0
    for delay in delays:
        sum_ += delay
    return sum_ / n
