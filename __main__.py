import asyncio

from configuration.settings import logger, dp, bot


async def main() -> None:
    import app
    await dp.start_polling(bot)
        
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())


# async def main() -> None:
    # from red_bot import app
    # await dp.start_polling(bot)