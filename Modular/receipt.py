import datetime


def print_receipt(order, order_type, subtotal, discount_rate,
                  discount_amount, promos, total):
    width = 42

    print()
    print("=" * width)
    print("CEBU DE GWAPO KAINAN".center(width))
    print("=" * width)
    print(f"Order Type: {order_type}".center(width))
    print(datetime.datetime.now().strftime("%m/%d/%Y  %I:%M %p").center(width))
    print("-" * width)
    print(f"|{'Item':<16}|{'Qty':>4}|{'Price':>9}|{'Total':>8}|")
    print("-" * width)

    for item_name, info in order.items():
        quantity = info["quantity"]
        price = info["price"]
        print(f"|{item_name:<16}|{quantity:>4}|{price:>9,.2f}|{price * quantity:>8,.2f}|")

    print("-" * width)
    print(f"|{'Subtotal:':<28}{subtotal:>13,.2f}|")

    if discount_amount > 0:
        label = f"Discount ({discount_rate * 100:.0f}%):"
        print(f"|{label:<28}{-discount_amount:>13,.2f}|")

    if promos["birthday"]:
        print("Happy Birthday! 15% promo applied.".center(width))

    if promos["pwd_senior"]:
        print("PWD/Senior 5% discount applied.".center(width))

    print(f"|{'TOTAL:':<28}{total:>13,.2f}|")
    print("=" * width)
    print("Salamat po sa inyong pagbisita!".center(width))
    print("Balik po kayo ulit!".center(width))
    print("=" * width)
    print()