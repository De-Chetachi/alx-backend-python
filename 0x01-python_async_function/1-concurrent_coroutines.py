#!/usr/bin/env python3
'''a module'''
import asyncio
import random
from typing import Union, List
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[Union[int, float]]:
    '''hmm oku'''
    delays = await asyncio.gather(*(wait_r(max_delay) for i in range(n)))
    return delays
