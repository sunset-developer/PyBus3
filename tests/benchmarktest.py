import asyncio
import random
from unittest import IsolatedAsyncioTestCase

import numpy

from pybus.pybus import *

bus = PyBus.instance()


class TestEvent:
    def __init__(self, min, max):
        self.min = min
        self.max = max


class TestClass:
    def __init__(self):
        bus.register(self)

    @subscribe(TestEvent)
    async def intensive(self, event):
        sorted(numpy.random.randint(0, high=event.min, size=event.max))


class BusTest(IsolatedAsyncioTestCase):

    async def test(self):
        TestClass()
        await bus.post(TestEvent(10000, 10000000))
        await bus.post(TestEvent(10000, 10000000))
