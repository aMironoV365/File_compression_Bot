from aiogram.filters import Command
from loader import dp, bot
import asyncio
from handlers.default_handlers.handler_start import send_welcome
from handlers.custom_handlers.handler_compress_pdf import compress_pdf
from handlers.default_handlers.commands import send_commands
from config_data.logger_config import setup_logging

setup_logging()


async def main():
    dp.message.register(send_welcome, Command("send_welcome"))
    dp.message.register(compress_pdf, Command("compress_pdf"))
    dp.message.register(send_commands, Command("send_commands"))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
