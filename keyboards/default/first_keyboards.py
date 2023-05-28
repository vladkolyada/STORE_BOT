from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


get_contact = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Give my own phone number', request_contact=True)
    ]
])

fruits_or_vegetables = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Fruits'),
        KeyboardButton('Vegetables')
    ]
])
