BOOK_DISCOUNT = 0.9

ELECTRONICS_DISCOUNT = 0.8

NO_DISCOUNT = 1.0

DISCOUNTS = {

    "book": BOOK_DISCOUNT,

    "electronics": ELECTRONICS_DISCOUNT

}

def calculate_total_price(items):

    total = 0

    for item in items:

        discount = DISCOUNTS.get(item["type"], NO_DISCOUNT)

        total += item["price"] * discount

    return total  

items = [

    {"type": "book", "price": 20},

    {"type": "electronics", "price": 100},

    {"type": "clothing", "price": 50}

]

print("Total price: £", calculate_total_price(items))
