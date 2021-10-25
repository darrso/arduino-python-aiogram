import serial

from aiogram import types
from aiogram.dispatcher import Dispatcher

import time
import sys

sys.path.append('python')
from config import aPort, aBaudrate
import pBttns

arduino = serial.Serial(port=aPort, baudrate=aBaudrate)
arduino.timeout = 1


async def leds(query: types.CallbackQuery):
    answer_data = query.data
    answer_data_1 = int(answer_data.split('_')[0])
    answer_data_2 = int(answer_data.split('_')[1])
    if answer_data_1 == 0:
        arduino.write(f"off_{pBttns.colors_1[answer_data_2]}".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка выключена!⚪️', reply_markup=pBttns.colors[answer_data_2])
    else:
        arduino.write(f"on_{pBttns.colors_1[answer_data_2]}".encode())
        time.sleep(0.5)
        await query.message.answer(f'Лампочка включена!{pBttns.colors_2[answer_data_2]}', reply_markup=pBttns.colors[answer_data_2])


def register_handlers_1(dp: Dispatcher):
    dp.register_callback_query_handler(leds, text=['0_0', '1_0', '0_1', '1_1', '0_2', '1_2'])