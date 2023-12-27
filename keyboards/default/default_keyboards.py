from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


get_contact = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Give my own phone number', request_contact=True)
    ]
], resize_keyboard=True)

remove_kb = ReplyKeyboardRemove()


def kb_for_basket(basket: list):
    kb_basket = [[KeyboardButton('Clear all from basket')]]
    for i in basket:
        kb_basket.append(
            [
                KeyboardButton(f'Delete {i}')
            ]
        )

    return ReplyKeyboardMarkup(keyboard=kb_basket)
