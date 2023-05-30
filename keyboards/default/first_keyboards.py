from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


get_contact = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Give my own phone number', request_contact=True)
    ]
], resize_keyboard=True)


