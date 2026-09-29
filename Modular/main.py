from menu import get_menu, display_menu
from yes_no import ask_yes_no
from order import get_order
from order_type import get_order_type
from promo import get_promos
from calculate import get_subtotal, get_discount, get_total
from receipt import print_receipt


def main():
    menu = get_menu()
    display_menu(menu)

    if not ask_yes_no("Would you like to place an order?"):
        print("\nThank you and Goodbye!")
        return

    order = get_order(menu)
    order_type = get_order_type()
    promos = get_promos()

    subtotal = get_subtotal(order)
    discount_rate, discount_amount = get_discount(subtotal, promos)
    total = get_total(subtotal, discount_amount)

    print_receipt(order, order_type, subtotal, discount_rate,
                  discount_amount, promos, total)


main()