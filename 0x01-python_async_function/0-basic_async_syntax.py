#!/usr/bin/env python3
'''a module ith asyn await'''
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    '''what is this?'''
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
