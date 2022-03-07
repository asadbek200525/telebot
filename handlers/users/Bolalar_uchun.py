from aiogram import types
from keyboards.inline.Bolalar_uchun import bolalar
from loader import dp


# Echo bot
@dp.message_handler(text='Bolalar uchun')
async def bot_echo(message: types.Message):
    await message.answer('Bolalar uchun',reply_markup=bolalar)