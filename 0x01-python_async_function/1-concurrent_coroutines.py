#!/usr/bin/env python3
'''a module'''
import asyncio
import random
from typing import Union, List
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''hmm oku'''
    delays = [asyncio.create_task(wait_r(max_delay)) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
