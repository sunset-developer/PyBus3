from unittest import IsolatedAsyncioTestCase
from pybus3.pybus import *

bus = AsyncPyBus.instance()


class TestEvent:
    def __init__(self, message):
        self.message = message


class TestClass:
    def __init__(self):
        bus.register(self)
        self.test_message = None

    @subscribe(TestEvent)
    async def subscribed(self, event):
        self.test_message = event.message


class BusTest(IsolatedAsyncioTestCase):
    async def test(self):
        test_class = TestClass()
        await bus.post(TestEvent('test message'))
        self.assertEqual(test_class.test_message, 'test message')
