from aiogram import types
from keyboards.default.Dasturlar import filmlar, dastur,kitoblar,oyin
from keyboards.default.MENU import asosiy
from loader import dp


@dp.message_handler(text="O'yinlar🎮")
async def bot_echo(message: types.Message):
    await message.answer('O\'yinlar sahifasi👇',reply_markup=oyin)

@dp.message_handler(text='Ilovalar📲')
async def bot_echo(message: types.Message):
    await message.answer('Ilovalar safifasi👇',reply_markup=dastur)

@dp.message_handler(text="Kitoblar📚")
async def bot_echo(message: types.Message):
    await message.answer('Kitoblar sahifasi👇',reply_markup=kitoblar)

@dp.message_handler(text="Filmlar🎥")
async def bot_echo(message: types.Message):
    await message.answer("Filmlar sahifasi👇",reply_markup=filmlar)

