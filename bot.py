import config
import logging

from aiogram import Bot, Dispacher, executor, types

#задаем уровень логов
logging.basicConfig(level=logging.INFO)

#инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispacher(bot)

# Эхо бот
@dp.messages_handler()
async def echo (message: type.Message):
    
