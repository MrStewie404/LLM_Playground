from manager.base import DB_manager as manager

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Инициализация бота и диспетчера
TOKEN = manager.get_token()
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Запуск бота
async def main():
    await dp.start_polling(bot)