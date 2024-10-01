import aiohttp


async def ClientFactory(url: str):
    # reusable connection make uses of keep-alive and connection-token
    # avoid to create multiple connexion
   return  aiohttp.ClientSession(url)
      