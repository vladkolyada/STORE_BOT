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


types_of_apples = InlineKeyboardMarkup(inline_keyboard=[
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

back_to_types_of_apples_or_buy_gd = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/apple/golden_delicious/buy_golden_delicious')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/apple')
    ]
])

back_to_types_of_apples_or_buy_idared = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/apple/idared/buy_idared')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/apple')
    ]
])


types_of_watermelons = InlineKeyboardMarkup(inline_keyboard=[
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


back_to_types_of_watermelons_or_buy_arsenal = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/watermelon/arsenal/buy_arsenal')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/watermelon')
    ]
])


back_to_types_of_watermelons_or_buy_sensei = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/watermelon/sensei/buy_sensei')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/watermelon')
    ]
])


types_of_grapes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Olymp', callback_data='/fruits/grape/olymp')
    ],
    [
        InlineKeyboardButton('Bianca', callback_data='/fruits/grape/bianca')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits')
    ]
])

back_to_types_of_grapes_or_buy_olymp = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/grape/olymp/buy_olymp')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/grape')
    ]
])

back_to_types_of_grapes_or_buy_bianca = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/grape/bianca/buy_bianca')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/grape')
    ]
])


types_of_bananas = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Cavendish', callback_data='/fruits/banana/cavendish')
    ],
    [
        InlineKeyboardButton('Morado', callback_data='/fruits/banana/morado')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits')
    ]
])

back_to_types_of_bananas_or_buy_cavendish = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/banana/cavendish/buy_cavendish')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/banana')
    ]
])

back_to_types_of_bananas_or_buy_morado = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Buy', callback_data='/fruits/banana/morado/buy_morado')
    ],
    [
        InlineKeyboardButton('Back', callback_data='/fruits/banana')
    ]
])
