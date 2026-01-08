from bot_init import bot
import importlib
import pkgutil
from pathlib import Path
from config import TOKEN

def load_modules(folder: str):
    package = importlib.import_module(folder)
    if not package.__file__:
        return
    dir_path = Path(package.__file__).parent
    for _, mod_name, _ in pkgutil.iter_modules([str(dir_path)]):
        importlib.import_module(f"{folder}.{mod_name}")

load_modules('commands')
load_modules('tasks')
load_modules('DBManager')
load_modules('event')

bot.run(TOKEN)