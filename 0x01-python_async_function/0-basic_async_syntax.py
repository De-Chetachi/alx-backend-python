#!/usr/bin/env python3
'''a module'''
import asyncio
import random


async def wait_random(max_delay: int = 10):
    '''what is this?'''
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran