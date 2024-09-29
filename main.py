from aiogram.filters import Command
from loader import dp, bot
import asyncio
from handlers.default_handlers.handler_start import send_welcome
from handlers.custom_handlers.handler_compress_pdf import compress_pdf
from config_data.logger_config import setup_logging

setup_logging()


async def main() -> None:
    """
    Основная асинхронная функция, которая регистрирует обработчики команд и запускает бота.

    Регистрирует обработчики для команд:
    - /send_welcome: Обрабатывает команду /start и отправляет приветственное сообщение.
    - /compress_pdf: Обрабатывает команду для сжатия PDF-файла.

    Запускает бота с использованием метода start_polling.
    """
    dp.message.register(send_welcome, Command("send_welcome"))
    dp.message.register(compress_pdf, Command("compress_pdf"))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
