import aiohttp, atexit, asyncio

# Classes:
import games
import user


class Client:
    def __init__(self):
        self.requests = aiohttp.ClientSession()
        self.Game = games(self.requests)
        self.User = user(self.requests)

        atexit.register(lambda: asyncio.run(self.shutdown()))

    async def shutdown(self):
        await self.requests.close()