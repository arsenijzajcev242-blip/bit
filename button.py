from aiogram.types import (
    InlineKeyboardButton,
    KeyboardButton
)
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    ReplyKeyboardBuilder
)

# Обычная клавиатура
main = ReplyKeyboardBuilder()

main.row(
    KeyboardButton(text='Профиль'),
    KeyboardButton(text='Корзина'),
    KeyboardButton(text='Меню')
)

# Inline-клавиатура
menu = InlineKeyboardBuilder()

menu.add(
    InlineKeyboardButton(
        text='Каталог',
        callback_data='catalog'
    )
)
