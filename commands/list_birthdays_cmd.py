from bot_init import bot
from bot_init import db
from disnake.ext.commands import has_any_role
from config import ROLE_COMMAND_ACCESS

@has_any_role(*ROLE_COMMAND_ACCESS)
@bot.command(name="list_birthdays")
async def list_birthdays_cmd(ctx):
    rows = await db.get_info_birthday()
    
    if not rows:
        await ctx.send("Нет записей.")
        return
    
    msg = "Дни рождения:\n"
    for row in rows:
        try:
            user = await bot.fetch_user(row[0])
            name = user.name
        except:
            name = f"User ID {row[0]}"
        date_str = row[1].strftime("%d-%m")
        msg += f"{name}: {date_str}\n"
    
    await ctx.send(msg)