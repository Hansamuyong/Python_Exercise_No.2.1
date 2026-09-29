def get_subtotal(order):
    total = 0

    for info in order.values():
        total += info["quantity"] * info["price"]

    return total


def get_discount(subtotal, promos):
    rate = 0

    if promos["birthday"]:
        rate += 0.15

    if promos["pwd_senior"]:
        rate += 0.05

    return rate, subtotal * rate


def get_total(subtotal, discount_amount):
    return subtotal - discount_amount