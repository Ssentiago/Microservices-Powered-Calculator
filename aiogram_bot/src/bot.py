import asyncio
import os
import sys

from aiogram import Bot, Dispatcher




from bot_menu.menu import set_menu
from config.config import load_config, Config
from config.log_config import *
from handlers import other_handlers, user_handlers


async def main():
    config: Config = load_config()
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.startup.register(set_menu)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
