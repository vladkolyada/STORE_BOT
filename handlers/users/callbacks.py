import os
from aiogram import types

from loader import dp
from states.steps import StatesForBot
from keyboards.inline.fruits.fruit_selection import types_of_fruits, sorts_of_apple, back_to_sorts_of_apple_or_buy_gd, \
    back_to_sorts_of_apple_or_buy_idared, sorts_of_watermelon, back_to_sorts_of_watermelon_or_buy_arsenal, \
    back_to_sorts_of_watermelon_or_buy_sensei, sorts_of_grape, back_to_sorts_of_grape_or_buy_bianca, \
    back_to_sorts_of_grape_or_buy_olymp, sorts_of_banana, back_to_sorts_of_banana_or_buy_cavendish, \
    back_to_sorts_of_banana_or_buy_morado
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
                                                    'Price per kilo: $1.00',
                                            reply_markup=back_to_sorts_of_apple_or_buy_idared)
    elif callback.data == '/fruits/watermelon':
        await callback.message.delete()
        await callback.message.answer(text='Choose apple sort.',
                                      reply_markup=sorts_of_watermelon)
    elif callback.data == '/fruits/watermelon/arsenal':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('arsenal.jpg')), 'rb'),
                                            caption='Watermelon sort - Arsenal\n'
                                                    'Price per kilo: $0.55',
                                            reply_markup=back_to_sorts_of_watermelon_or_buy_arsenal)
    elif callback.data == '/fruits/watermelon/sensei':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('sensei.jpg')), 'rb'),
                                            caption='Watermelon sort - Sensei\n'
                                                    'Price per kilo: $0.60',
                                            reply_markup=back_to_sorts_of_watermelon_or_buy_sensei)
    elif callback.data == '/fruits/grape':
        await callback.message.delete()
        await callback.message.answer(text='Choose grape sort',
                                      reply_markup=sorts_of_grape)
    elif callback.data == '/fruits/grape/olymp':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('olymp.jpg')), 'rb'),
                                            caption='Grape sort - Olymp\n'
                                                    'Price per kilo: $2.35',
                                            reply_markup=back_to_sorts_of_grape_or_buy_olymp)
    elif callback.data == '/fruits/grape/bianca':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('bianca.jpg')), 'rb'),
                                            caption='Grape sort - Bianca\n'
                                                    'Price per kilo: $2.10',
                                            reply_markup=back_to_sorts_of_grape_or_buy_bianca)
    elif callback.data == '/fruits/banana':
        await callback.message.delete()
        await callback.message.answer(text='Choose grape sort',
                                      reply_markup=sorts_of_banana)
    elif callback.data == '/fruits/banana/cavendish':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('cavendish.jpg')), 'rb'),
                                            caption='Banana sort - Cavendish\n'
                                                    'Price per kilo: $2.95',
                                            reply_markup=back_to_sorts_of_banana_or_buy_cavendish)
    elif callback.data == '/fruits/banana/morado':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('morado.jpg')), 'rb'),
                                            caption='Banana sort - Morado\n'
                                                    'Price per kilo: $3.20',
                                            reply_markup=back_to_sorts_of_banana_or_buy_morado)
    elif callback.data == '/back':
        await callback.message.delete()
        await callback.message.answer(text='Choose type of product.',
                                      reply_markup=fruits_or_vegetables)



