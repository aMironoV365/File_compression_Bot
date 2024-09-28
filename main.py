from aiogram.filters import Command

from loader import dp, bot
import asyncio
import logging
from handlers.default_handlers.handler_start import send_welcome
from handlers.custom_handlers.handler_compress_pdf import compress_pdf
from handlers.default_handlers.commands import send_commands


logging.basicConfig(level=logging.INFO)


async def main():
    dp.message.register(send_welcome, Command("send_welcome"))
    dp.message.register(compress_pdf, Command("compress_pdf"))
    dp.message.register(send_commands, Command("send_commands"))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
