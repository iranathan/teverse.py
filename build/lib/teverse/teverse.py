import aiohttp, atexit, asyncio

# Classes:
from .game import Game
from .user import User


class Client:
    def __init__(self):
        self.requests = aiohttp.ClientSession()
        self.Game = Game(self.requests)
        self.User = User(self.requests)

        atexit.register(lambda: asyncio.run(self.shutdown()))

    async def shutdown(self):
        await self.requests.close()