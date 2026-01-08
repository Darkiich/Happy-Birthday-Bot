from disnake.ext import tasks
from config import CHANNEL_ID
from bot_init import bot, db
from datetime import datetime

@tasks.loop(hours=12)
async def check_birthdays():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    request = await db.get_info_birthday()
    if not request:
        return "Не удалось получить данные при запуске задачи"
    
    today = datetime.now().strftime("%d-%m")

    for row in request:
        if row[1].strftime("%d-%m") == today:
            try:
                user = await bot.fetch_user(row[0])
                await channel.send(f"Сегодня день рождения у {user.mention}!\nПоздравляю тебя! 🎉")
            except:
                pass