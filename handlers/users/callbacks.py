import os
from aiogram import types

from loader import dp
from states.steps import StatesForBot
from keyboards.inline.fruits.fruit_selection import types_of_fruits, sorts_of_apple, back_to_sorts_of_apple_or_buy_gd
from keyboards.inline.vegetables.vegetable_selection import types_of_vegetables
from keyboards.inline.default_keyboard import fruits_or_vegetables


@dp.callback_query_handler(state=StatesForBot.AfterAuthorization)
async def fruit_or_vegetables(callback: types.CallbackQuery):
    # selection between fruits and vegetables
    if callback.data == '/fruits':
        await callback.message.delete()
        await callback.message.answer(text='Choose type of fruit.',
                                      reply_markup=types_of_fruits)
    elif callback.data == '/vegetables':
        await callback.message.delete()
        await callback.message.answer(text='Choose type of vegetable.',
                                      reply_markup=types_of_vegetables)

    # fruits
    elif callback.data == '/fruits/apple':
        await callback.message.delete()
        await callback.message.answer(text='Choose apple sort.',
                                      reply_markup=sorts_of_apple)
    elif callback.data == '/fruits/apple/golden_delicious':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('golden_delicious.jpg')), 'rb'),
                                            caption='Apple sort - Golden Delicious\n'
                                                    'Price per kilo: $1.63',
                                            reply_markup=back_to_sorts_of_apple_or_buy_gd)
    elif callback.data == '/fruits/apple/idared':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('idared.jpg')), 'rb'),
                                            caption='Apple sort - Idared\n'
                                                    'Price per kilo: $1.00')
    elif callback.data == '/back':
        await callback.message.delete()
        await callback.message.answer(text='Go shopping! Choose type of product.',
                                      reply_markup=fruits_or_vegetables)



