from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


types_of_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Potato 🥔', callback_data='/vegetable/apple')
    ],
    [
        InlineKeyboardButton('Tomato 🍅', callback_data='/vegetable/watermelon')
    ],
    [
        InlineKeyboardButton('Corn 🌽', callback_data='/vegetable/grape')
    ],
    [
        InlineKeyboardButton('Carrot 🥕', callback_data='/vegetable/banana')
    ]
])

