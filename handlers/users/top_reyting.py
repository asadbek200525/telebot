from aiogram import types
from keyboards.inline.Top_reyting import ilova_reyting,oyin_reyting
from loader import dp


# Echo bot
@dp.message_handler(text='Top reyting')
async def bot_echo(message: types.Message):
    await message.answer('(oyin nomlari)',reply_markup=oyin_reyting)

@dp.message_handler(text='Top reyting ')
async def bot_echo(message: types.Message):
    await message.answer('(ilova nomlari)',reply_markup=ilova_reyting)