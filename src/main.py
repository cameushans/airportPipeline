import asyncio
from dotenv import load_dotenv
from utils.env_builder import *
from utils.get_token import *
import aiohttp

load_dotenv()

async def main():
    # reusable connection make uses of keep-alive and connection-token
    # avoid to create multiple connexion 
    async with aiohttp.ClientSession(injectEnv('BASE_NIFI_URL')) as session:
        try:
            token = await get_token(injectEnv('AUTH_URL'), session, injectEnv('USERNAME'), injectEnv('PASSWORD'))
            if not token:
                return
            
            async with session.get(injectEnv('PROCESSORS'), headers={'Authorization': f'Bearer {token}'}, ssl=False) as response:       
                if response.status == 200:
                    data = await response.json()
                    print(f"Response body: {data}") 
                else:
                    print(f"Erreur: {response.status}")
                    print(await response.text())

        except aiohttp.ClientConnectorError as e:
            print(f"Erreur de connexion: {e}")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

asyncio.run(main())