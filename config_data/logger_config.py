import logging


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filemode='a',
                        filename='compression_bot.log',
                        datefmt='%d/%m/%Y %H:%M:%S')
