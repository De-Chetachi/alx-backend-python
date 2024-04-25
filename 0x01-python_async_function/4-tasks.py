#!/usr/bin/env python3
'''a module'''
import asyncio
import random
from typing import Union, List
t_wait_r = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''hmm oku'''
    delays = [t_wait_r(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
