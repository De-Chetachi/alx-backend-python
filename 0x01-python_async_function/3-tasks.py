#!/usr/bin/env python3
'''a module'''
import asyncio
import random
from typing import Union, List, Awaitable
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    '''hmm oku'''
    return asyncio.create_task(wait_r(max_delay))
