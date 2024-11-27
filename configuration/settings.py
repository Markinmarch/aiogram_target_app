import logging
import os
from redis import Redis

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from .config import (
    BOT_TOKEN,
    REDIS_HOST,
    REDIS_PORT,
    REDIS_BD
)


def logs():
    if 'aiogram_app.log' not in os.listdir('.'):
        with open('aiogram_app.log', mode = 'x', encoding = 'utf-8') as log_file:
            log_file.close()
    else:
        pass

    logging.basicConfig(
        format = '%(asctime)s %(name)s %(levelname)s %(message)s',
        level = logging.INFO,
        handlers = [
            logging.FileHandler('aiogram_app.log'),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger(__name__)

bot = Bot(
    token = BOT_TOKEN
)

storage = RedisStorage(
    redis = Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD
    )
)

dp = Dispatcher()
