from aiogram import types
from keyboards.default.MENU import asosiy
from keyboards.default.Dasturlar import filmlar, dastur,kitoblar,oyin
from loader import dp

@dp.message_handler(text='Orqaga⬅️')
async def bot_echo(message: types.Message):
    await message.answer('Bosh sahifa👇',reply_markup=asosiy)

@dp.message_handler(text='Bosh sahifa')
async def bot_echo(message: types.Message):
    await message.answer('Bosh sahifa👇',reply_markup=asosiy)

@dp.message_handler(text='Orqaga')
async def bot_echo(message: types.Message):
    await message.answer('O\'yinlar sahifasi👇',reply_markup=oyin)

@dp.message_handler(text='Orqaga ')
async def bot_echo(message: types.Message):
    await message.answer('Ilovalar safifasi👇',reply_markup=dastur)


