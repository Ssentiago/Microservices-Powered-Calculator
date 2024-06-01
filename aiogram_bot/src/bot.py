import asyncio
import os
import sys

from aiogram import Bot, Dispatcher

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '..', 'inline_keyboard'))
sys.path.append(os.path.join(current_dir, '..', 'service'))


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

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await dp.startup.register(set_menu)


if __name__ == '__main__':
    asyncio.run(main())
