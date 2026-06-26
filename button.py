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
main = main.as_markup(resize_keyboard=True) 
# Inline-клавиатура
menu = InlineKeyboardBuilder()

menu.add(
    InlineKeyboardButton(
        text='Каталог',
        callback_data='catalog'
    )
)
menu = menu.as_markup()
