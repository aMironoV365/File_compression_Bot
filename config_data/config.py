import os
from dotenv import load_dotenv, find_dotenv


def load_environment_variables() -> None:
    """
    Загружает переменные окружения из файла .env.
    Если файл .env отсутствует, программа завершается с сообщением об ошибке.
    """
    if not find_dotenv():
        exit("Переменные окружения не загружены т.к отсутствует файл .env")
    else:
        load_dotenv()


def get_bot_token() -> str:
    """
    Возвращает токен бота, загруженный из переменных окружения.
    Если токен не найден, программа завершается с сообщением об ошибке.
    """
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        exit("Токен бота не найден в переменных окружения")
    return bot_token


# Загрузка переменных окружения
load_environment_variables()

# Получение токена бота
BOT_TOKEN = get_bot_token()
