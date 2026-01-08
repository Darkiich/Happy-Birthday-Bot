from bot_init import bot
from bot_init import db
from datetime import datetime
from disnake.ext.commands import has_any_role
from config import ROLE_COMMAND_ACCESS

@has_any_role(*ROLE_COMMAND_ACCESS)
@bot.command(name="update_birthday")
async def update_birthday_cmd(ctx, date: str):
    ds_id = ctx.author.id
    
    date = date.replace('.', '-')
    
    try:
        this_date = datetime.strptime(date, "%d-%m")
    except ValueError:
        await ctx.send("Невалидный формат записи. Используй DD.MM")
        return

    request = await db.update_birthday(ds_id, this_date)
    
    if request == 0:
        await ctx.send("Не найдена запись для обновления. Используй $add_birthday.")
        return
    
    await ctx.send(f"Дата рождения обновлена до {date} для {ctx.author.name}.")