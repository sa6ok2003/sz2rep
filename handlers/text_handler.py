from aiogram import types
from misc import dp,bot
import asyncio



My_id = 494588959
#{"id": -1001405664089, "title": "Проверка учасника", "username": "movie_bots", "type": "channel"}

@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    if int(message.chat.id) == 494588959:
        await bot.send_message(chat_id=message.chat.id,text=message.text)