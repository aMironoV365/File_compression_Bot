import logging


def setup_logging() -> logging.Logger:
    """
    Настраивает логирование для приложения.

    Уровень логирования устанавливается на INFO.
    Формат сообщений логирования:
    - %(asctime)s: Время события.
    - %(name)s: Имя логгера.
    - %(levelname)s: Уровень логирования.
    - %(message)s: Сообщение логгера.

    Логи записываются в файл 'compression_bot.log' в режиме добавления ('a').
    Формат даты и времени: '%d/%m/%Y %H:%M:%S'.
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filemode='a',
                        filename='compression_bot.log',
                        datefmt='%d/%m/%Y %H:%M:%S')
