from aiohttp import ClientSession
from utils.SessionFactory import *

async def processors(session: ClientSession, url: str, token: str): 
        try:
            async with session.get(url, headers={'Authorization': f'Bearer {token}'}, ssl=False) as response:       
                if response.status == 200:
                    print(f"Success") 
                    print(await response.json())
                else:
                    print(f"Erreur: {response.status}")
                    print(await response.text())

        except aiohttp.ClientConnectorError as e:
            print(f"Erreur de connexion: {e}")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

