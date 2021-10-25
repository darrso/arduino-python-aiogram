from aiogram import types
from aiogram.dispatcher import Dispatcher

import sys
sys.path.append('python')

import pBttns


async def start_command(message: types.Message):
    await message.answer('Привет!', reply_markup = pBttns.bttns)
async def choose(message: types.Message):
    if message.text == "Красная лампочка🔴":
        await message.answer("Выберите действие с 🔴красной🔴 лампочкой:", reply_markup = pBttns.colors[0])
    elif message.text == "Желтая лампочка🟡":
        await message.answer("Выберите действие с 🟡желтой🟡 лампочкой:", reply_markup = pBttns.colors[1])
    else:
        await message.answer("Выберите действие с 🟢зеленой🟢 лампочкой:", reply_markup = pBttns.colors[2])

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(choose, text = ["Красная лампочка🔴", "Желтая лампочка🟡", "Зеленая лампочка🟢"])
    dp.register_message_handler(start_command, commands = "start")