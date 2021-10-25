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
    if answer_data == "0_0":
        arduino.write("off_red".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка выключена!⚪️', reply_markup = pBttns.colors[0])
    elif answer_data == "1_0":
        arduino.write("on_red".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка включена!🔴', reply_markup = pBttns.colors[0])
    elif answer_data == "0_1":
        arduino.write("off_yel".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка выключена!⚪️', reply_markup = pBttns.colors[1])
    elif answer_data == "1_1":
        arduino.write("on_yel".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка включена!🟡', reply_markup = pBttns.colors[1])
    elif answer_data == "0_2":
        arduino.write("off_gre".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка выключена!⚪️', reply_markup = pBttns.colors[2])
    else:
        arduino.write("on_gre".encode())
        time.sleep(0.5)
        await query.message.answer('Лампочка включена!🟢', reply_markup = pBttns.colors[2])

def register_handlers_1(dp: Dispatcher):
    dp.register_callback_query_handler(leds, text = ['0_0', '1_0', '0_1', '1_1', '0_2', '1_2'])