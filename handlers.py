from aiogram import  types, F, Router

from app.button import menu, main
from aiogram.filters import CommandStart, Command

router = Router()
users = {}

@router.message(Command('start'))
print("NEW START HANDLER")
async def echo(message: types.Message):
    await message.answer('Привет,как ты?',reply_markup=menu.as_markup())

@router.message(F.photo)
async def pgoto(message: types.Message):
    photo = message.photo[-1].file_id
    users[message.from_user.id] = photo
    await message.answer("Фото сохранено.")
@router.message(Command('get_photo'))
async def get_photo(message: types.Message):
    us_id = message.from_user.id
    if us_id in users:
        await message.answer_photo(photo=users[us_id])
    else:
        await message.answer('Вы еще не отправляли фото', reply_markup=menu)

