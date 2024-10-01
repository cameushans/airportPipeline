from functools import lru_cache, wraps
from aiohttp import ClientSession
from cerberus import * 

async def get_token(url: str, session: ClientSession, username: str, password: any ) -> str | None:
    hash = dict()
    async with session.post(url, data={'username': username, 'password': password}, ssl=False) as response:
        if response.status == 201:
            hash['token'] = await response.text()
            hash['csrf'] = response.cookies['__Secure-Request-Token'].value
            
            return hash
        else:
            print(f"Échec de l'obtention du token. Status: {response.status}")
            print(await response.text())
            return None