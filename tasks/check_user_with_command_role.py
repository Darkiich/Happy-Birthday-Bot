from disnake.ext import tasks
from disnake.errors import NotFound
from bot_init import bot, db
from config import ROLE_COMMAND_ID, CHANNEL_ID, GUILD_ID, LOG_CHANNEL_ID

@tasks.loop(hours=12)
async def check_user():
    list_users = await db.get_info_birthday()
    channel = bot.get_channel(CHANNEL_ID)
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    guild = bot.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_COMMAND_ID)

    if not list_users:
        await channel.send("При запуске бота не нашлось записей.")
        return

    for row in list_users:
        try:
            member = await guild.fetch_member(row[0])

            if role not in member.roles:
                await db.remove_birthday(row[0])
                await log_channel.send(f"Удалил пользователя {row[0]} из БД (нет роли)")

        except NotFound:
            await db.remove_birthday(row[0])
            await log_channel.send(f"Удалил пользователя {row[0]} из БД (не найден)")

        except Exception as e:
            await channel.send(f"Ошибка: {e}")