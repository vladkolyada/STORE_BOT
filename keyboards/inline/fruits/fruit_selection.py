from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


type_of_fruits = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Apple 🍏', callback_data='fruit/apple')
    ],
    [
        InlineKeyboardButton('Watermelon 🍉', callback_data='fruit/watermelon')
    ],
    [
        InlineKeyboardButton('Grape 🍇', callback_data='fruit/grape')
    ],
    [
        InlineKeyboardButton('Banana 🍌', callback_data='fruit/banana')
    ]
])

