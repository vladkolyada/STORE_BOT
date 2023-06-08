from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


types_of_fruits = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Apple 🍏', callback_data='/fruits/apple')
    ],
    [
        InlineKeyboardButton('Watermelon 🍉', callback_data='/fruits/watermelon')
    ],
    [
        InlineKeyboardButton('Grape 🍇', callback_data='/fruits/grape')
    ],
    [
        InlineKeyboardButton('Banana 🍌', callback_data='/fruits/banana')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/back')
    ]
])

sorts_of_apple = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Golden Delicious', callback_data='/fruits/apple/golden_delicious')
    ],
    [
        InlineKeyboardButton('Idared', callback_data='/fruits/apple/idared')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits')
    ]
])

back_to_sorts_of_apple_or_buy_gd = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/apple/golden_delicious/buy_golden_delicious')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/apple')
    ]
])

back_to_sorts_of_apple_or_buy_idared = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/apple/idared/buy_idared')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/apple')
    ]
])

sorts_of_watermelon = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Arsenal', callback_data='/fruits/watermelon/arsenal')
    ],
    [
        InlineKeyboardButton('Sensei', callback_data='/fruits/watermelon/sensei')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits')
    ]
])
