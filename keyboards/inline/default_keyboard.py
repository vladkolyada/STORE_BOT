from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


fruits_or_vegetables = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Fruits 🍇', callback_data='/fruits'),
        InlineKeyboardButton('Vegetables 🥕', callback_data='/vegetables')
    ],
    [
        InlineKeyboardButton('Check basket', callback_data='/check_basket')
    ],
    [
        InlineKeyboardButton('Send order', callback_data='/send_order')
    ]
])


def add_kilo(name_of_type_of_product: str):
    add_kilogram = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('+', callback_data=f'/+/{name_of_type_of_product}'),
            InlineKeyboardButton('-', callback_data=f'/-/{name_of_type_of_product}')
        ],
        [
            InlineKeyboardButton('Put in basket', callback_data=f'/add_product/{name_of_type_of_product}')
        ],
        [
            InlineKeyboardButton('Back', callback_data='/back')
        ]
    ])
    return add_kilogram


def kb_for_remove_product_from_basket_fruits(name_of_type_of_product: str):
    remove_p = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Remove product from basket',
                                 callback_data=f'/delete_product_from_basket/{name_of_type_of_product}')
        ],
        [
            InlineKeyboardButton('Back to fruits', callback_data='/fruits')
        ]
    ])
    return remove_p


def kb_for_remove_product_from_basket_vegetables(name_of_type_of_product: str):
    remove_p = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Remove product from basket',
                                 callback_data=f'/delete_product_from_basket/{name_of_type_of_product}')
        ],
        [
            InlineKeyboardButton('Back to vegetables', callback_data='/vegetables')
        ]
    ])
    return remove_p


kb_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Back', callback_data='/back')
    ]
])

