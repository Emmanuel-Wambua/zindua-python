products = {
    {"name":"Boots", "price":1500},
    {"name":"t-shirt", "price":500},
    {"name":"Laptop", "price":25000},
    {"name":"Gum", "price":340}
}

def find_highest_price(products):
    highest_price = 0
    highest_priced_product = None

    for product in products:
        if product["price"] > highest_price:
            highest_price = product["price"]
            highest_priced_product = product

    return highest_priced_product

outcome = find_highest_price(products)

print(outcome)