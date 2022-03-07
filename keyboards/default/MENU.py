from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

asosiy =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'yinlar🎮"),
            KeyboardButton(text='Ilovalar📲')
        ],
        [
            KeyboardButton(text="Filmlar🎥"),
            KeyboardButton(text="Kitoblar📚")
        ],
        [
            KeyboardButton(text='ADMIN👨‍💻')
        ],
    ],resize_keyboard=True
)

