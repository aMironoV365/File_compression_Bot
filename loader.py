from aiogram import Bot, Dispatcher
from config_data.config import BOT_TOKEN


def initialize_bot() -> Bot:
    """
    Инициализирует объект бота с использованием токена, полученного из переменных окружения.

    Возвращает:
    - Bot: Инициализированный объект бота.
    """
    return Bot(token=BOT_TOKEN)


def initialize_dispatcher() -> Dispatcher:
    """
    Инициализирует объект диспетчера для обработки сообщений.

    Возвращает:
    - Dispatcher: Инициализированный объект диспетчера.
    """
    return Dispatcher()


# Инициализация бота и диспетчера
bot = initialize_bot()
dp = initialize_dispatcher()
