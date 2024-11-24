import logging
import os


def logger():
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


# def main():
#     if __name__ == "__main__":
#         from DB.main_db import database, create_table
#         from app import app_settings
#         database
#         create_table
#         app_settings.dp.run(debug=True)
# logger()
# main()

# logging.basicConfig(
#     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level = logging.INFO
# )
# logger = logging.getLogger(__name__)
# =====================================================
# bot = Bot(
#     token = BOT_TOKEN,
#     parse_mode = 'HTML'
# )

# storage = RedisStorage(
#     redis = Redis(
#         host = REDIS_HOST,
#         port = REDIS_PORT,
#         db = REDIS_BD
#     )
# )

# dp = Dispatcher()

# async def main() -> None:
#     from red_bot import app
#     await dp.start_polling(bot)