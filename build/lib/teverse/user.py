class User:
    def __init__(self, requests):
        self.requests = requests

    async def get_user_by_id(self, tid: str) -> dict:
        r = await self.requests.get(f'https://teverse.com/api/users/{tid}')
        return await r.json()

    async def get_user_games(self, tid: str) -> list:
        r = await self.requests.get(f'https://teverse.com/api/users/{tid}/games')
        return await r.json()
