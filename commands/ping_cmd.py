from bot_init import bot


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Понг")