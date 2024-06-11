#!/usr/bin/env python3

"""0. Async Generator"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator that yields 10 random numbers between 0 and 10"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
