basket = []


async def add_product_to_basket(product: str):
    global basket
    basket.append(product)


async def delete_product_from_basket(product: str):
    global basket
    basket.remove(product)


async def clear_all_from_basket():
    global basket
    basket.clear()


async def check_data(message):
    await message.answer(text='\n\n'.join(basket))
