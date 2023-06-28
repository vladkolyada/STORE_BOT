from keyboards.default.default_keyboards import kb_for_basket


basket = []


async def add_product_to_basket(product):
    global basket
    basket.append(product)


async def delete_product_from_basket(product: str):
    global basket
    basket.remove(product)


async def clear_all_from_basket():
    global basket
    basket.clear()


async def check_data(message, total_price):
    if not basket:
        await message.answer(text='The basket is clean')
    else:
        data = '\n\n'.join(basket)
        await message.answer(text=f"{data}\n\n"
                                  f"Total price: ${total_price:.2f}",
                             reply_markup=kb_for_basket(basket=basket))


async def send_the_order_to_the_group(bot, message, first_name, last_name, group_id, phone_number, total_price):
    global basket
    if not basket:
        await message.answer(text='The basket is clean')
    else:
        order = f'\n\n'.join(basket)
        basket = []
        if last_name is None:
            last_name = ''
        elif first_name is None:
            first_name = ''
        await bot.send_message(chat_id=group_id, text=f'{phone_number}, \n'
                                                      f'{first_name} {last_name}\n\n'
                                                      f'{order}\n\n'
                                                      f'Total price: ${total_price:.2f}')
        await message.answer(text='Thank you for your order! See you later.')
