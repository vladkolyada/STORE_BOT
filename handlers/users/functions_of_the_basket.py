basket = []


async def update_basket(data_of_product: str):
    global basket
    basket.append(data_of_product)


async def remove_same_product_from_basket(data_of_product: str):
    global basket
    basket.remove(data_of_product)


async def remove_all_products_from_basket():
    global basket
    basket.clear()

