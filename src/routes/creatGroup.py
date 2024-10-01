from aiohttp import ClientSession
from utils.SessionFactory import *

async def createGroup(session: ClientSession, url: str, token: str, csrf: str): 
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        'Request-Token': csrf
        }
        
        data = {
          'component': {
                'name': 'Mon Nouveau Groupe'
            },
            'revision': {
                'version': 0
            }
        }
        
        try:
            async with session.post(url, headers=headers, json=data, ssl=False) as response:       
                if response.status == 201:
                    data = response.json()
                    print(f"Success: CREATED group") 
                    print(await data)
                else:
                    print(f"Erreur: {response.status}")
                    print(await response.text())
        except aiohttp.ClientConnectorError as e:
            print(f"Erreur de connexion: {e}")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")