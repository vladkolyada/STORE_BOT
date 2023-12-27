from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


types_of_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
<<<<<<< HEAD
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
=======
        InlineKeyboardButton('Potato 🥔', callback_data='/vegetables/potato')
    ],
    [
        InlineKeyboardButton('Tomato 🍅', callback_data='/vegetables/tomato')
    ],
    [
        InlineKeyboardButton('Corn 🌽', callback_data='/vegetables/corn')
    ],
    [
        InlineKeyboardButton('Carrot 🥕', callback_data='/vegetables/carrot')
>>>>>>> e8322c99f5faa915b4d96712cca669e167a2c250
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
<<<<<<< HEAD
        InlineKeyboardButton('Back', callback_data='/vegetables/tomatoes')
=======
        InlineKeyboardButton('Back', callback_data='/vegetables/tomato')
>>>>>>> e8322c99f5faa915b4d96712cca669e167a2c250
    ]
])

back_to_types_of_tomatoes_or_buy_beefsteak = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/tomato/beefsteak/buy_beefsteak')
    ],
    [
<<<<<<< HEAD
        InlineKeyboardButton('Back', callback_data='/vegetables/tomatoes')
    ]
])
=======
        InlineKeyboardButton('Back', callback_data='/vegetables/tomato')
    ]
])


types_of_corns = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Sweet', callback_data='/vegetables/corn/sweet')
    ],
    [
        InlineKeyboardButton('Flint', callback_data='/vegetables/corn/flint')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables')
    ]
])

back_to_types_of_corns_or_buy_sweet = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/corn/sweet/buy_sweet')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/corn')
    ]
])

back_to_types_of_corns_or_buy_flint = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/corn/flint/buy_flint')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/corn')
    ]
])


types_of_carrots = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Danvers', callback_data='/vegetables/carrot/danvers')
    ],
    [
        InlineKeyboardButton('Nantes', callback_data='/vegetables/carrot/nantes')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables')
    ]
])

back_to_types_of_carrots_or_buy_danvers = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/carrot/danvers/buy_danvers')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/carrot')
    ]
])

back_to_types_of_carrots_or_buy_nantes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/carrot/nantes/buy_nantes')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/vegetables/carrot')
    ]
])
>>>>>>> e8322c99f5faa915b4d96712cca669e167a2c250
