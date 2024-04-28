#!/usr/bin/env python3
'''a module ith asyn await'''
import asyncio
import random


async def async_generator() -> float:
    '''async function'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
