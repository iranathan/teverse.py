class Game:
    def __init__(self, requests):
        self.requests = requests

    async def get_games(self) -> list:
        r = await self.requests.get(f'https://teverse.com/api/games/')
        return await r.json()