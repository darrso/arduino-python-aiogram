import asyncio

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from python.config import bToken

from python.handlers.message_handlers import *
from python.handlers.query_handlers import *

# bToken - in python/config.py insert your token
# bToken - в python/config.py вставьте свой токен

# register_handlers - python/handlers/message_handlers.py
# register_handlers_1 - python/handlers/query_handlers.py

async def main():
    bot = Bot(token=bToken)
    dp = Dispatcher(bot, storage=MemoryStorage()) #--BOT--

    register_handlers(dp)
    register_handlers_1(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())