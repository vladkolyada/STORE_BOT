from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


types_of_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Potato 🥔', callback_data='/vegetable/potato')
    ],
    [
        InlineKeyboardButton('Tomato 🍅', callback_data='/vegetable/tomato')
    ],
    [
        InlineKeyboardButton('Corn 🌽', callback_data='/vegetable/corn')
    ],
    [
        InlineKeyboardButton('Carrot 🥕', callback_data='/vegetable/carrot')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/back')
    ]
])


types_of_potatoes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Russet', callback_data='/vegetables/potato/russet')
    ],
    [
        InlineKeyboardButton('Kennebec', callback_data='/vegetables/potato/kennebec')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables')
    ]
])

back_to_types_of_potatoes_or_buy_russet = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/potato/russet/buy_russet')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/potato')
    ]
])

back_to_types_of_potatoes_or_buy_kennebec = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/potato/kennebec/buy_kennebec')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/potato')
    ]
])


types_of_tomatoes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Alicante', callback_data='/vegetables/tomato/alicante')
    ],
    [
        InlineKeyboardButton('Beefsteak', callback_data='/vegetables/tomato/beefsteak')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables')
    ]
])

back_to_types_of_tomatoes_or_buy_alicante = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/tomato/alicante/buy_alicante')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/tomatoes')
    ]
])

back_to_types_of_tomatoes_or_buy_beefsteak = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/tomato/beefsteak/buy_beefsteak')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/tomatoes')
    ]
])
