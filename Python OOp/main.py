from order import Order


def main():
    order = Order()

    order.display_menu()

    if not order.ask_yes_no("Would you like to place an order?"):
        print("\nThank you and Goodbye!")
        return

    order.get_order()
    order.get_order_type()
    order.get_promos()
    order.get_print()


if __name__ == "__main__":
    main()