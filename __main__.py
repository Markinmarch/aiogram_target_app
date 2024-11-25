import asyncio

from configuration.settings import logger, dp, bot


if __name__ == '__main__':
    async def main() -> None:
        await dp.start_polling(bot)
    try:
        asyncio.run(main())
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())


# async def main() -> None:
    # from red_bot import app
    # await dp.start_polling(bot)