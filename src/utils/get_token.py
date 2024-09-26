from aiohttp import ClientSession

async def get_token(url: str, session: ClientSession, username: str, password: any ):
    async with session.post(url, data={'username': username, 'password': password}, ssl=False) as response:
        if response.status == 201:
            return await response.text()
        else:
            print(f"Échec de l'obtention du token. Status: {response.status}")
            return None