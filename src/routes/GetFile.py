from aiohttp import ClientSession
from utils.SessionFactory import *

async def createProcessors(session: ClientSession, url: str, token: str): 
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
        try:
            async with session.post(url, headers=headers, json=processor_data, ssl=False) as response:       
                if response.status == 201:
                    data = await response.json()
                    print(f"Success: CREATED PROC") 
                    print(await data)
                else:
                    print(f"Erreur: {response.status}")
                    print(await response.text())
        except aiohttp.ClientConnectorError as e:
            print(f"Erreur de connexion: {e}")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")
            

processor_data = {
    "revision": {
        "version": 0
    },
    "component": {
        "parentGroupId": "026c2d7c-0192-1000-6dff-8f19fdaa7775",
        "position": {
            "x": 100,
            "y": 100
        },
        "name": "My Python Processor",
        "type": "org.apache.nifi.processors.standard.GetFile",
        "state": "STOPPED",
            "schedulingPeriod": "0 sec",
            "schedulingStrategy": "TIMER_DRIVEN",
            "executionNode": "ALL",
            "concurrentlySchedulableTaskCount": 1,
            "comments": "Processor created via Python",
            "autoTerminatedRelationships": []
        }
    }
