from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


types_of_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
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
        InlineKeyboardButton('Back', callback_data='/vegetables/tomato')
    ]
])

back_to_types_of_tomatoes_or_buy_beefsteak = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/vegetables/tomato/beefsteak/buy_beefsteak')
    ],
    [
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