import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '8753338258:AAHkpPFzt6uJMJ2DKUF-_jAvMJI_746WIZ4'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer('Привет')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())








my = '318591874ars'