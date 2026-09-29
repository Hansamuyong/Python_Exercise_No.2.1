from yes_no import ask_yes_no


def get_quantity():
    while True:
        quantity = input("Enter the quantity: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print("Invalid quantity. Please enter a whole number greater than 0.\n")


def display_order(order):
    print("=" * 42)
    print("CURRENT ORDER".center(42))
    print("=" * 42)
    print(f"|{'Item':<20}|{'Qty':>5}|{'Price':>8}|{'Subtotal':>9}|")
    print("-" * 42)

    for item_name, info in order.items():
        quantity = info["quantity"]
        price = info["price"]
        print(f"|{item_name:<20}|{quantity:>5}|{price:>8,.2f}|{quantity * price:>9,.2f}|")

    print("-" * 42)


def get_order(menu):
    order = {}

    while True:
        while True:
            item_name = input("Enter the menu item you want to order: ").strip().title()

            if item_name in menu:
                break

            print("Sorry, that item is not on the menu. Please check spelling.\n")

        quantity = get_quantity()

        if item_name in order:
            order[item_name]["quantity"] += quantity
        else:
            order[item_name] = {"quantity": quantity, "price": menu[item_name]}

        display_order(order)

        if not ask_yes_no("Do you want to order another item?"):
            return order