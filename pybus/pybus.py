class PyBus:
    _registered = []
    _subscribed = {}
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead.')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    async def post(self, posted_event):
        subscribed = {key: value for (key, value) in self._subscribed.items() if value == posted_event.__class__}
        for subscriber in subscribed:
            registrants = filter(lambda r: subscriber.__name__ in dir(r), self._registered)
            for registrant in registrants:
                await subscriber(registrant, posted_event)

    def register(self, registrant):
        self._registered.append(registrant)

    def subscribe(self, subscriber, event):
        self._subscribed[subscriber] = event


def subscribe(*args, **kwargs):
    def inner(func):
        event = kwargs['event'] if args[0] is None else args[0]
        PyBus.instance().subscribe(func, event)
        return func

    return inner
