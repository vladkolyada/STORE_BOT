import os
from aiogram import types

from loader import dp
from states.steps import StatesForBot
from keyboards.inline.fruits.fruit_selection import types_of_fruits, \
    types_of_apples, back_to_types_of_apples_or_buy_gd, back_to_types_of_apples_or_buy_idared, types_of_watermelons, \
    back_to_types_of_watermelons_or_buy_arsenal, back_to_types_of_watermelons_or_buy_sensei, types_of_grapes, \
    back_to_types_of_grapes_or_buy_bianca, back_to_types_of_grapes_or_buy_olymp, types_of_bananas, \
    back_to_types_of_bananas_or_buy_cavendish, back_to_types_of_bananas_or_buy_morado
from keyboards.inline.vegetables.vegetable_selection import types_of_vegetables, types_of_tomatoes, \
    back_to_types_of_tomatoes_or_buy_alicante, back_to_types_of_tomatoes_or_buy_beefsteak, \
    types_of_potatoes, back_to_types_of_potatoes_or_buy_kennebec, back_to_types_of_potatoes_or_buy_russet, \
    types_of_corns, back_to_types_of_corns_or_buy_sweet, back_to_types_of_corns_or_buy_flint, \
    types_of_carrots, back_to_types_of_carrots_or_buy_nantes, back_to_types_of_carrots_or_buy_danvers
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
    # only for apple
    # different sorts of apple
    elif callback.data == '/fruits/apple':
        await callback.message.delete()
        await callback.message.answer(text='Choose apple sort.',
                                      reply_markup=types_of_apples)
    elif callback.data == '/fruits/apple/golden_delicious':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('golden_delicious_apple.jpg')), 'rb'),
                                            caption='Apple sort - Golden Delicious\n'
                                                    'Price per kilo: $1.63',
                                            reply_markup=back_to_types_of_apples_or_buy_gd)
    elif callback.data == '/fruits/apple/idared':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('idared_apple.jpg')), 'rb'),
                                            caption='Apple sort - Idared\n'
                                                    'Price per kilo: $1.00',
                                            reply_markup=back_to_types_of_apples_or_buy_idared)
    # only for watermelon
    # different sorts of watermelon
    elif callback.data == '/fruits/watermelon':
        await callback.message.delete()
        await callback.message.answer(text='Choose watermelon sort.',
                                      reply_markup=types_of_watermelons)
    elif callback.data == '/fruits/watermelon/arsenal':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('arsenal_watermelon.jpg')), 'rb'),
                                            caption='Watermelon sort - Arsenal\n'
                                                    'Price per kilo: $0.55',
                                            reply_markup=back_to_types_of_watermelons_or_buy_arsenal)
    elif callback.data == '/fruits/watermelon/sensei':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('sensei_watermelon.jpg')), 'rb'),
                                            caption='Watermelon sort - Sensei\n'
                                                    'Price per kilo: $0.60',
                                            reply_markup=back_to_types_of_watermelons_or_buy_sensei)
    # only for grape
    # different sorts of grape
    elif callback.data == '/fruits/grape':
        await callback.message.delete()
        await callback.message.answer(text='Choose grape sort',
                                      reply_markup=types_of_grapes)
    elif callback.data == '/fruits/grape/olymp':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('olymp_grape.jpg')), 'rb'),
                                            caption='Grape sort - Olymp\n'
                                                    'Price per kilo: $2.35',
                                            reply_markup=back_to_types_of_grapes_or_buy_olymp)
    elif callback.data == '/fruits/grape/bianca':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('bianca_grape.jpg')), 'rb'),
                                            caption='Grape sort - Bianca\n'
                                                    'Price per kilo: $2.10',
                                            reply_markup=back_to_types_of_grapes_or_buy_bianca)
    # only for banana
    elif callback.data == '/fruits/banana':
        await callback.message.delete()
        await callback.message.answer(text='Choose banana sort',
                                      reply_markup=types_of_bananas)
    # different sorts of banana
    elif callback.data == '/fruits/banana/cavendish':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('cavendish_banana.jpg')), 'rb'),
                                            caption='Banana sort - Cavendish\n'
                                                    'Price per kilo: $2.95',
                                            reply_markup=back_to_types_of_bananas_or_buy_cavendish)
    elif callback.data == '/fruits/banana/morado':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('morado_banana.jpg')), 'rb'),
                                            caption='Banana sort - Morado\n'
                                                    'Price per kilo: $3.20',
                                            reply_markup=back_to_types_of_bananas_or_buy_morado)
    # vegetables
    # only for tomato
    elif callback.data == '/vegetables/tomato':
        await callback.message.delete()
        await callback.message.answer(text='Choose types of tomatoes',
                                      reply_markup=types_of_tomatoes)
    # different types of tomatoes
    elif callback.data == '/vegetables/tomato/alicante':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('alicante_tomato.jpg')), 'rb'),
                                            caption="Tomato type - Alicante\n"
                                                    "Price per kilo: $2.22",
                                            reply_markup=back_to_types_of_tomatoes_or_buy_alicante)
    elif callback.data == '/vegetables/tomato/beefsteak':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('beefsteak_tomato.jpg')), 'rb'),
                                            caption="Tomato type - Beefsteak\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_tomatoes_or_buy_beefsteak)
    # only for potato
    elif callback.data == '/vegetables/potato':
        await callback.message.delete()
        await callback.message.answer(text='Choose types of potatoes',
                                      reply_markup=types_of_potatoes)
    # different types of potatoes
    elif callback.data == '/vegetables/potato/kennebec':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('kennebec_potato.jpg')), 'rb'),
                                            caption="Potato type - Kennebec\n"
                                                    "Price per kilo: $2.22",
                                            reply_markup=back_to_types_of_potatoes_or_buy_kennebec)
    elif callback.data == '/vegetables/potato/russet':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('russet_potato.jpg')), 'rb'),
                                            caption="Potato type - Russet\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_potatoes_or_buy_russet)
    # only for corn
    elif callback.data == '/vegetables/corn':
        await callback.message.delete()
        await callback.message.answer(text='Choose types of corns',
                                      reply_markup=types_of_corns)
    # different types of corns
    elif callback.data == '/vegetables/corn/sweet':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('sweet_corn.jpg')), 'rb'),
                                            caption="Corn type - Sweet\n"
                                                    "Price per kilo: $2.22",
                                            reply_markup=back_to_types_of_corns_or_buy_sweet)
    elif callback.data == '/vegetables/corn/flint':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('flint_corn.jpg')), 'rb'),
                                            caption="Corn type - Flint\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_corns_or_buy_flint)
    # only for carrot
    elif callback.data == '/vegetables/carrot':
        await callback.message.delete()
        await callback.message.answer(text='Choose types of carrots',
                                      reply_markup=types_of_carrots)
    # different types of carrots
    elif callback.data == '/vegetables/carrot/danvers':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('danvers_carrot.jpg')), 'rb'),
                                            caption="Carrot type - Danvers\n"
                                                    "Price per kilo: $2.22",
                                            reply_markup=back_to_types_of_carrots_or_buy_danvers)
    elif callback.data == '/vegetables/carrot/nantes':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('nantes_carrot.jpg')), 'rb'),
                                            caption="Carrot type - Nantes\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_carrots_or_buy_nantes)
    # back to selection between fruits and vegetables
    elif callback.data == '/back':
        await callback.message.delete()
        await callback.message.answer(text='Choose type of product.',
                                      reply_markup=fruits_or_vegetables)



