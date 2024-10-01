import asyncio
from dotenv import load_dotenv
from utils.SessionFactory import ClientFactory
from utils.env_builder import injectEnv
from utils.get_token import get_token
from routes.creatGroup import createGroup


load_dotenv()

async def main():
    async with await ClientFactory(injectEnv('BASE_NIFI_URL')) as session:
        token = await get_token(injectEnv('AUTH_URL'), session, injectEnv('USERNAME'), injectEnv('PASSWORD'))
        
        await createGroup(session,injectEnv('CREATE_GROUP'), token['token'], token['csrf'] )
asyncio.run(main())
# will trigger all tasks specified in the main 