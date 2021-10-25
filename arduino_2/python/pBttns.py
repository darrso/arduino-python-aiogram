from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

# bttns - LED selection buttons
bttns = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
bttn_red, bttn_yel, bttn_gre = KeyboardButton('Красная лампочка🔴'), KeyboardButton('Желтая лампочка🟡'), KeyboardButton('Зеленая лампочка🟢')
bttns.add(bttn_red, bttn_yel, bttn_gre)

# colors - list of inline buttons (each LED has its own)
red_lamp, yel_lamp, gre_lamp = None, None, None
colors = [red_lamp, yel_lamp, gre_lamp]
count = 0
for i in range(len(colors)):
    a = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (
        ('Включить✅', f'1_{count}'), ('Выключить✖️', f'0_{count}')
    )
    a_1 = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    a.add(*a_1)
    colors[i] = a
    count += 1