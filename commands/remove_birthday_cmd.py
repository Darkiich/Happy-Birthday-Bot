from bot_init import bot, db
from disnake.ext.commands import has_any_role
from config import ROLE_COMMAND_ACCESS

@has_any_role(*ROLE_COMMAND_ACCESS)
@bot.command(name="remove_birthday")
async def remove_birthday_cmd(ctx):
    ds_id = ctx.author.id
    
    request = await db.remove_birthday(ds_id)
    
    await ctx.send("Запись удалена.") if request > 0 else await ctx.send("Запись не найдена.")
