from aiogram import types, F
from aiogram.filters import Command
from loader import dp


COMMANDS = [
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("compress", "Сжать изображение без потерь качества"),
    ("commands", "Вывести список команд")
]


@dp.message(Command("commands"))
@dp.message(F.text.lower().in_(["команды", "список команд"]))
async def send_commands(message: types.Message):
    commands_text = "\n".join([f"/{command} - {description}" for command, description in COMMANDS])
    await message.reply(f"Доступные команды:\n{commands_text}")

