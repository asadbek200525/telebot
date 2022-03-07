from aiogram import types
from keyboards.default.Turkumlar import oyin_t,ilova_t
from loader import dp


# Echo bot
@dp.message_handler(text='Turkumlar')
async def bot_echo(message: types.Message):
    await message.answer('Turkumlarni tanlang', reply_markup=oyin_t)

@dp.message_handler(text='Turkumlar ')
async def bot_echo(message: types.Message):
    await message.answer('Turkumlarni tanlang', reply_markup=ilova_t)
