from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


fruits_or_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Fruits 🍇', callback_data='fruits'),
        InlineKeyboardButton('Vegetables 🥕', callback_data='vegetables')
    ]
])

