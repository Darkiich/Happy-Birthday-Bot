from dotenv import load_dotenv
import os

load_dotenv()

def get_env(key: str, default=None):
    value = os.getenv(key)
    if value is None:
        return default
    return value

TOKEN = get_env("DISCORD_BOT_TOKEN")
USER = get_env("USER_DB")
PASSWORD = get_env("PASSWORD")
HOST = get_env("URL")
PORT = int(get_env("PORT"))
DATABASE = get_env("NAME_DB")
CHANNEL_ID = 1055439905402130464 # командный канал
LOG_CHANNEL_ID = 1141810442721833060 # лог канал
ROLE_COMMAND_ID = 1428866954403512513 # роль команды
GUILD_ID = 901772674865455115 # сервер

ROLE_COMMAND_ACCESS = [
    1428866954403512513 # роль команды
]