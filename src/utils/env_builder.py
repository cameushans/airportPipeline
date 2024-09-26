from dotenv import load_dotenv
import os 

load_dotenv()

hash = dict(
BASE_NIFI_URL = os.getenv('BASE_NIFI_URL'),
ENVIRONMENT = os.getenv('ENV'),
AUTH_URL = os.getenv('AUTH_URL'),
USERNAME = os.getenv('NIFI_USERNAME'),
PASSWORD = os.getenv('NIFI_PASSWORD'),
PROCESSORS = os.getenv('PROCESSORS')
)

def injectEnv(env: str) -> str | None:
    return hash[env]