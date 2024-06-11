#!/usr/bin/env python3

"""0. Async Generator"""
import asyncio
import random


async def async_generator():
    """Generator that yields random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
