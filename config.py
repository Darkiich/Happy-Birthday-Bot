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
CHANNEL_ID = 1396199253189328981 # командный канал
LOG_CHANNEL_ID = 1426139098384568361 # лог канал
ROLE_COMMAND_ID = 1432780044475830292 # роль команды
GUILD_ID = 1396199251117346856 # сервер

ROLE_COMMAND_ACCESS = [
    1432780044475830292 # роль команды
]