import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from config import TOKEN

users = {}
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer('Привет')

@dp.message(F.photo)
async def pgoto(message: types.Message):
    photo = message.photo[-1].file_id
    users[message.from_user.id] = photo
    await message.answer("Фото сохранено.")
@dp.message(Command('get_photo'))
async def get_photo(message: types.Message):
    us_id = message.from_user.id
    if us_id in users:
        await message.answer_photo(photo=users[us_id])
    else:
        await message.answer('Вы еще не отправляли фото')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')








my = '318591874ars'
