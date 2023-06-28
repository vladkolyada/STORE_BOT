import os
import re
from aiogram import types

from loader import dp, db, bot
from data.config import GROUP
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
from keyboards.inline.default_keyboard import fruits_or_vegetables, add_kilo, \
    kb_for_remove_product_from_basket_fruits, kb_back, kb_for_remove_product_from_basket_vegetables
from .functions_for_basket import add_product_to_basket, delete_product_from_basket, \
    check_data, send_the_order_to_the_group

price = 0
kilograms = 0
total_price = 0


async def clear_price(current_price):
    global total_price
    total_price -= float(f"{current_price:.2f}")


@dp.callback_query_handler(state=StatesForBot.AfterAuthorization)
async def fruit_or_vegetables(callback: types.CallbackQuery):
    global price, kilograms, total_price
    # selection between fruits and vegetables
    if abs(price) < 0.01:
        price = 0
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
    elif callback.data == '/fruits/apple':
        await callback.message.delete()
        await callback.message.answer(text='Choose apple sort.',
                                      reply_markup=types_of_apples)
    # different sorts of apple
    elif callback.data == '/fruits/apple/golden_delicious':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('golden_delicious_apple.jpg')), 'rb'),
                                            caption='Apple sort - Golden Delicious\n'
                                                    'Price per kilo: $1.63',
                                            reply_markup=back_to_types_of_apples_or_buy_gd)
    elif callback.data == '/fruits/apple/golden_delicious/buy_golden_delicious':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Apple sort - Golden Delicious\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("golden_delicious"))
    elif callback.data == "/+/golden_delicious":
        kilograms += 1
        price += 1.63
        total_price += 1.63
        await callback.message.edit_caption(caption=f'Apple sort - Golden Delicious\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("golden_delicious"))
    elif callback.data == "/-/golden_delicious":
        kilograms -= 1
        price -= 1.63
        total_price -= 1.63
        await callback.message.edit_caption(caption=f'Apple sort - Golden Delicious\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("golden_delicious"))
    elif callback.data == '/add_product/golden_delicious':
        await add_product_to_basket(f'Apple sort - Golden Delicious\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Apple Golden Delicious added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("golden_delicious"))
    elif callback.data == '/delete_product_from_basket/golden_delicious':
        await delete_product_from_basket(f'Apple sort - Golden Delicious\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/fruits/apple/idared':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('idared_apple.jpg')), 'rb'),
                                            caption='Apple sort - Idared\n'
                                                    'Price per kilo: $1.00',
                                            reply_markup=back_to_types_of_apples_or_buy_idared)
    elif callback.data == '/fruits/apple/idared/buy_idared':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Apple sort - Idared\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("idared"))
    elif callback.data == "/+/idared":
        kilograms += 1
        price += 1.00
        total_price += 1.00
        await callback.message.edit_caption(caption=f'Apple sort - Idared\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("idared"))
    elif callback.data == "/-/idared":
        kilograms -= 1
        price -= 1.00
        total_price -= 1.00
        await callback.message.edit_caption(caption=f'Apple sort - Idared\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("idared"))
    elif callback.data == '/add_product/idared':
        await add_product_to_basket(f'Apple sort - Idared\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Apple Idared added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("idared"))
    elif callback.data == '/delete_product_from_basket/idared':
        await delete_product_from_basket(f'Apple sort - Idared\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    # only for watermelon
    elif callback.data == '/fruits/watermelon':
        await callback.message.delete()
        await callback.message.answer(text='Choose watermelon sort.',
                                      reply_markup=types_of_watermelons)
    # different sorts of watermelon
    elif callback.data == '/fruits/watermelon/arsenal':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('arsenal_watermelon.jpg')), 'rb'),
                                            caption='Watermelon sort - Arsenal\n'
                                                    'Price per kilo: $0.55',
                                            reply_markup=back_to_types_of_watermelons_or_buy_arsenal)
    elif callback.data == '/fruits/watermelon/arsenal/buy_arsenal':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Watermelon sort - Arsenal\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("arsenal"))
    elif callback.data == "/+/arsenal":
        kilograms += 1
        price += 0.55
        total_price += 0.55
        await callback.message.edit_caption(caption=f'Watermelon sort - Arsenal\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("arsenal"))
    elif callback.data == "/-/arsenal":
        kilograms -= 1
        price -= 0.55
        total_price -= 0.55
        await callback.message.edit_caption(caption=f'Watermelon sort - Arsenal\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("arsenal"))
    elif callback.data == '/add_product/arsenal':
        await add_product_to_basket(f'Watermelon sort - Arsenal\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Watermelon Arsenal added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("arsenal"))
    elif callback.data == '/delete_product_from_basket/arsenal':
        await delete_product_from_basket(f'Watermelon sort - Arsenal\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/fruits/watermelon/sensei':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('sensei_watermelon.jpg')), 'rb'),
                                            caption='Watermelon sort - Sensei\n'
                                                    'Price per kilo: $0.60',
                                            reply_markup=back_to_types_of_watermelons_or_buy_sensei)
    elif callback.data == '/fruits/watermelon/sensei/buy_sensei':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Watermelon sort - Sensei\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sensei"))
    elif callback.data == "/+/sensei":
        kilograms += 1
        price += 0.60
        total_price += 0.60
        await callback.message.edit_caption(caption=f'Watermelon sort - Sensei\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sensei"))
    elif callback.data == "/-/sensei":
        kilograms -= 1
        price -= 0.60
        total_price -= 0.60
        await callback.message.edit_caption(caption=f'Watermelon sort - Sensei\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sensei"))
    elif callback.data == '/add_product/sensei':
        await add_product_to_basket(f'Watermelon sort - Sensei\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Watermelon Sensei added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("sensei"))
    elif callback.data == '/delete_product_from_basket/sensei':
        await delete_product_from_basket(f'Watermelon sort - Sensei\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    # only for grape
    elif callback.data == '/fruits/grape':
        await callback.message.delete()
        await callback.message.answer(text='Choose grape sort',
                                      reply_markup=types_of_grapes)
    # different sorts of grape
    elif callback.data == '/fruits/grape/olymp':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('olymp_grape.jpg')), 'rb'),
                                            caption='Grape sort - Olymp\n'
                                                    'Price per kilo: $2.35',
                                            reply_markup=back_to_types_of_grapes_or_buy_olymp)
    elif callback.data == '/fruits/grape/olymp/buy_olymp':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Grape sort - Olymp\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("olymp"))
    elif callback.data == "/+/olymp":
        kilograms += 1
        price += 2.35
        total_price += 2.35
        await callback.message.edit_caption(caption=f'Grape sort - Olymp\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("olymp"))
    elif callback.data == "/-/olymp":
        kilograms -= 1
        price -= 2.35
        total_price -= 2.35
        await callback.message.edit_caption(caption=f'Grape sort - Olymp\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("olymp"))
    elif callback.data == '/add_product/olymp':
        await add_product_to_basket(f'Grape sort - Olymp\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Grape Olymp added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("olymp"))
    elif callback.data == '/delete_product_from_basket/olymp':
        await delete_product_from_basket(f'Grape sort - Olymp\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/fruits/grape/bianca':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('bianca_grape.jpg')), 'rb'),
                                            caption='Grape sort - Bianca\n'
                                                    'Price per kilo: $2.10',
                                            reply_markup=back_to_types_of_grapes_or_buy_bianca)
    elif callback.data == '/fruits/grape/bianca/buy_bianca':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Grape sort - Bianca\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("bianca"))
    elif callback.data == "/+/bianca":
        kilograms += 1
        price += 2.10
        total_price += 2.10
        await callback.message.edit_caption(caption=f'Grape sort - Bianca\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("bianca"))
    elif callback.data == "/-/bianca":
        kilograms -= 1
        price -= 2.10
        total_price -= 2.10
        await callback.message.edit_caption(caption=f'Grape sort - Bianca\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("bianca"))
    elif callback.data == '/add_product/bianca':
        await add_product_to_basket(f'Grape sort - Bianca\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Grape Bianca added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("bianca"))
    elif callback.data == '/delete_product_from_basket/bianca':
        await delete_product_from_basket(f'Grape sort - Bianca\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
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
    elif callback.data == '/fruits/banana/cavendish/buy_cavendish':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Banana sort - Cavendish\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("cavendish"))
    elif callback.data == "/+/cavendish":
        kilograms += 1
        price += 2.95
        total_price += 2.95
        await callback.message.edit_caption(caption=f'Banana sort - Cavendish\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("cavendish"))
    elif callback.data == "/-/cavendish":
        kilograms -= 1
        price -= 2.95
        total_price -= 2.95
        await callback.message.edit_caption(caption=f'Banana sort - Cavendish\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("cavendish"))
    elif callback.data == '/add_product/cavendish':
        await add_product_to_basket(f'Banana sort - Cavendish\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Banana Cavendish added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("cavendish"))
    elif callback.data == '/delete_product_from_basket/cavendish':
        await delete_product_from_basket(f'Banana sort - Cavendish\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/fruits/banana/morado':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('morado_banana.jpg')), 'rb'),
                                            caption='Banana sort - Morado\n'
                                                    'Price per kilo: $3.20',
                                            reply_markup=back_to_types_of_bananas_or_buy_morado)
    elif callback.data == '/fruits/banana/morado/buy_morado':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Banana sort - Morado\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("morado"))
    elif callback.data == "/+/morado":
        kilograms += 1
        price += 3.20
        total_price += 3.20
        await callback.message.edit_caption(caption=f'Banana sort - Morado\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("morado"))
    elif callback.data == "/-/morado":
        kilograms -= 1
        price -= 3.20
        total_price -= 3.20
        await callback.message.edit_caption(caption=f'Banana sort - Morado\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("morado"))
    elif callback.data == '/add_product/morado':
        await add_product_to_basket(f'Banana sort - Morado\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Banana Morado added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_fruits("morado"))
    elif callback.data == '/delete_product_from_basket/morado':
        await delete_product_from_basket(f'Banana sort - Morado\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
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
    elif callback.data == '/vegetables/tomato/alicante/buy_alicante':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Tomato type - Alicante\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("alicante"))
    elif callback.data == "/+/alicante":
        kilograms += 1
        price += 2.22
        total_price += 2.22
        await callback.message.edit_caption(caption=f'Tomato type - Alicante\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("alicante"))
    elif callback.data == "/-/alicante":
        kilograms -= 1
        price -= 2.22
        total_price -= 2.22
        await callback.message.edit_caption(caption=f'Tomato type - Alicante\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("alicante"))
    elif callback.data == '/add_product/alicante':
        await add_product_to_basket(f'Tomato type - Alicante\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Tomato Alicante added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("alicante"))
    elif callback.data == '/delete_product_from_basket/alicante':
        await delete_product_from_basket(f'Tomato type - Alicante\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/vegetables/tomato/beefsteak':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('beefsteak_tomato.jpg')), 'rb'),
                                            caption="Tomato type - Beefsteak\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_tomatoes_or_buy_beefsteak)
    elif callback.data == '/vegetables/tomato/beefsteak/buy_beefsteak':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Tomato type - Beefsteak\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("beefsteak"))
    elif callback.data == "/+/beefsteak":
        kilograms += 1
        price += 5.55
        total_price += 5.55
        await callback.message.edit_caption(caption=f'Tomato type - Beefsteak\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("beefsteak"))
    elif callback.data == "/-/beefsteak":
        kilograms -= 1
        price -= 5.55
        total_price -= 5.55
        await callback.message.edit_caption(caption=f'Tomato type - Beefsteak\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("beefsteak"))
    elif callback.data == '/add_product/beefsteak':
        await add_product_to_basket(f'Tomato type - Beefsteak\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Tomato Beefsteak added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("beefsteak"))
    elif callback.data == '/delete_product_from_basket/beefsteak':
        await delete_product_from_basket(f'Tomato type - Beefsteak\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
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
    elif callback.data == '/vegetables/potato/kennebec/buy_kennebec':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Potato type - Kennebec\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("kennebec"))
    elif callback.data == "/+/kennebec":
        kilograms += 1
        price += 2.22
        total_price += 2.22
        await callback.message.edit_caption(caption=f'Potato type - Kennebec\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("kennebec"))
    elif callback.data == "/-/kennebec":
        kilograms -= 1
        price -= 2.22
        total_price -= 2.22
        await callback.message.edit_caption(caption=f'Potato type - Kennebec\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("kennebec"))
    elif callback.data == '/add_product/kennebec':
        await add_product_to_basket(f'Potato type - Kennebec\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Potato Kennebec added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("kennebec"))
    elif callback.data == '/delete_product_from_basket/kennebec':
        await delete_product_from_basket(f'Potato type - Kennebec\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/vegetables/potato/russet':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('russet_potato.jpg')), 'rb'),
                                            caption="Potato type - Russet\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_potatoes_or_buy_russet)
    elif callback.data == '/vegetables/potato/russet/buy_russet':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Potato type - Russet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("russet"))
    elif callback.data == "/+/russet":
        kilograms += 1
        price += 5.55
        total_price += 5.55
        await callback.message.edit_caption(caption=f'Potato type - Russet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("russet"))
    elif callback.data == "/-/russet":
        kilograms -= 1
        price -= 5.55
        total_price -= 5.55
        await callback.message.edit_caption(caption=f'Potato type - Russet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("russet"))
    elif callback.data == '/add_product/russet':
        await add_product_to_basket(f'Potato type - Russet\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Potato Russet added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("russet"))
    elif callback.data == '/delete_product_from_basket/russet':
        await delete_product_from_basket(f'Potato type - Russet\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
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
    elif callback.data == '/vegetables/corn/sweet/buy_sweet':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Corn type - Sweet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sweet"))
    elif callback.data == "/+/sweet":
        kilograms += 1
        price += 2.22
        total_price += 2.22
        await callback.message.edit_caption(caption=f'Corn type - Sweet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sweet"))
    elif callback.data == "/-/sweet":
        kilograms -= 1
        price -= 2.22
        total_price -= 2.22
        await callback.message.edit_caption(caption=f'Corn type - Sweet\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("sweet"))
    elif callback.data == '/add_product/sweet':
        await add_product_to_basket(f'Corn type - Sweet\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Corn Sweet added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("sweet"))
    elif callback.data == '/delete_product_from_basket/sweet':
        await delete_product_from_basket(f'Corn type - Sweet\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/vegetables/corn/flint':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('flint_corn.jpg')), 'rb'),
                                            caption="Corn type - Flint\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_corns_or_buy_flint)
    elif callback.data == '/vegetables/corn/flint/buy_flint':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Corn type - Flint\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("flint"))
    elif callback.data == "/+/flint":
        kilograms += 1
        price += 5.55
        total_price += 5.55
        await callback.message.edit_caption(caption=f'Corn type - Flint\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("flint"))
    elif callback.data == "/-/flint":
        kilograms -= 1
        price -= 5.55
        total_price -= 5.55
        await callback.message.edit_caption(caption=f'Corn type - Flint\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("flint"))
    elif callback.data == '/add_product/flint':
        await add_product_to_basket(f'Corn type - Flint\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Corn Flint added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("flint"))
    elif callback.data == '/delete_product_from_basket/flint':
        await delete_product_from_basket(f'Corn type - Flint\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
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
    elif callback.data == '/vegetables/carrot/danvers/buy_danvers':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Carrot type - Danvers\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("danvers"))
    elif callback.data == "/+/danvers":
        kilograms += 1
        price += 2.22
        total_price += 2.22
        await callback.message.edit_caption(caption=f'Carrot type - Danvers\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("danvers"))
    elif callback.data == "/-/danvers":
        kilograms -= 1
        price -= 2.22
        total_price -= 2.22
        await callback.message.edit_caption(caption=f'Carrot type - Danvers\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("danvers"))
    elif callback.data == '/add_product/danvers':
        await add_product_to_basket(f'Carrot type - Danvers\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Carrot Danvers added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("danvers"))
    elif callback.data == '/delete_product_from_basket/danvers':
        await delete_product_from_basket(f'Carrot type - Danvers\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/vegetables/carrot/nantes':
        await callback.message.delete()
        await callback.message.answer_photo(photo=open(str(os.path.abspath('nantes_carrot.jpg')), 'rb'),
                                            caption="Carrot type - Nantes\n"
                                                    "Price per kilo: $5.55",
                                            reply_markup=back_to_types_of_carrots_or_buy_nantes)
    elif callback.data == '/vegetables/carrot/nantes/buy_nantes':
        kilograms = 0
        price = 0
        await callback.message.edit_caption(caption=f'Carrot type - Nantes\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("nantes"))
    elif callback.data == "/+/nantes":
        kilograms += 1
        price += 5.55
        total_price += 5.55
        await callback.message.edit_caption(caption=f'Carrot type - Nantes\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("nantes"))
    elif callback.data == "/-/nantes":
        kilograms -= 1
        price -= 5.55
        total_price -= 5.55
        await callback.message.edit_caption(caption=f'Carrot type - Nantes\n'
                                                    f'{kilograms}kg - ${price:.2f}',
                                            reply_markup=add_kilo("nantes"))
    elif callback.data == '/add_product/nantes':
        await add_product_to_basket(f'Carrot type - Nantes\n'
                                    f'{kilograms}kg - ${price:.2f}')
        await callback.message.edit_caption(caption='Carrot Nantes added to basket',
                                            reply_markup=kb_for_remove_product_from_basket_vegetables("nantes"))
    elif callback.data == '/delete_product_from_basket/nantes':
        await delete_product_from_basket(f'Carrot type - Nantes\n'
                                         f'{kilograms}kg - ${price:.2f}')
        await callback.message.delete()
        await callback.message.answer(text='Product deleted from basket', reply_markup=kb_back)
    elif callback.data == '/check_basket':
        await check_data(message=callback.message, total_price=total_price)
    elif callback.data == '/send_order':
        data = await db.take_a_data(callback.message.chat.id)
        await send_the_order_to_the_group(bot=bot, first_name=data[0][1],
                                          last_name=data[0][2], group_id=GROUP,
                                          phone_number=data[0][0], total_price=total_price,
                                          message=callback.message)
        total_price = 0
    # back to selection between fruits and vegetables
    elif callback.data == '/back':
        await callback.message.delete()
        await callback.message.answer(text='Choose type of product.',
                                      reply_markup=fruits_or_vegetables)


@dp.message_handler(state=StatesForBot.AfterAuthorization)
async def texts(message: types.Message):
    global total_price
    if message.text:
        for i in message.text.split():
            if i == "Delete":
                await delete_product_from_basket(product=message.text[7:])
                matches = re.findall(r'\d+\.\d+', message.text)
                for match in matches:
                    text_price = float(match)
                    total_price -= text_price
                await check_data(message=message, total_price=total_price)
            else:
                pass
