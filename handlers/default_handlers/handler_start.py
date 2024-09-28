from aiogram import types
from aiogram.filters.command import Command
from loader import dp
from config_data.logger_config import setup_logging

setup_logging()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}! Я бот для уменьшения размера твоих PDF файлов, "
                         f"отправь мне файл в чат и я уменьшу его размер")
