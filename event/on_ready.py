from bot_init import bot
from tasks.attention_happy_birthday import check_birthdays
from tasks.check_user_with_command_role import check_user

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')
    check_birthdays.start()
    check_user.start()