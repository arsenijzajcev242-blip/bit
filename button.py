from aiogram.types import (InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder , ReplyKeyboardBuilder , ReplyKeyboardMarkup

main = ReplyKeyboardBuilder()
btn1 = KeyboardButton(text='Профиль')
btn2 = KeyboardButton(text='Корзина')
btn3 = KeyboardButton(text='Меню')
main.row(btn1,btn2,btn3)
menu = InlineKeyboardBuilder()
btn1menu = InlineKeyboardButton(text='Каталог',callback_data = 'btn1')
menu.add(btn1menu)
