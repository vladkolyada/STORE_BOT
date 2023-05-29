def add_product_to__basket(basket: list, product: str):
    basket.append(product)


def delete_product_from_basket(basket: list, product: str):
    basket.remove(product)


def clear_all_from_basket(basket: list):
    basket.clear()
