import datetime


class Order:
    MENU = {
        "Adobong Manok": 120.00,
        "Sinigang Na Baboy": 150.00,
        "Lechon Kawali": 160.00,
        "Pancit Canton": 90.00,
        "Sisig": 140.00,
        "Kare-Kare": 170.00,
        "Tapsilog": 110.00,
        "Lumpiang Shanghai": 80.00,
        "Halo-Halo": 95.00,
        "Buko Juice": 45.00
    }

    def __init__(self):
        self.items = {}
        self.order_type = ""
        self.promos = {"birthday": False, "pwd_senior": False}

    def ask_yes_no(self, question):
        while True:
            answer = input(question + " [yes|no]: ").strip().lower()

            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print("Invalid input. Please type 'yes' or 'no'.\n")

    def display_menu(self):
        print("=" * 42)
        print("CEBU DE GWAPO KAINAN MENU".center(42))
        print("=" * 42)
        print(f"|{'Item':<25}|{'Price':>14}|")
        print("-" * 42)

        for item, price in self.MENU.items():
            print(f"|{item:<25}|{'P' + format(price, ',.2f'):>14}|")

        print("-" * 42)
        print()

    def get_quantity(self):
        while True:
            quantity = input("Enter the quantity: ").strip()

            if quantity.isdigit() and int(quantity) > 0:
                return int(quantity)

            print("Invalid quantity. Please enter a whole number greater than 0.\n")

    def display_order(self):
        print("=" * 42)
        print("CURRENT ORDER".center(42))
        print("=" * 42)
        print(f"|{'Item':<20}|{'Qty':>5}|{'Price':>8}|{'Subtotal':>9}|")
        print("-" * 42)

        for item_name, info in self.items.items():
            quantity = info["quantity"]
            price = info["price"]
            print(f"|{item_name:<20}|{quantity:>5}|{price:>8,.2f}|{quantity * price:>9,.2f}|")

        print("-" * 42)

    def get_order(self):
        while True:
            while True:
                item_name = input("Enter the menu item you want to order: ").strip().title()

                if item_name in self.MENU:
                    break

                print("Sorry, that item is not on the menu. Please check spelling.\n")

            quantity = self.get_quantity()
            if item_name in self.items:
                self.items[item_name]["quantity"] += quantity
            else:
                self.items[item_name] = {"quantity": quantity, "price": self.MENU[item_name]}

            self.display_order()

            if not self.ask_yes_no("Do you want to order another item?"):
                return

    def get_order_type(self):
        while True:
            choice = input("Dine In or Take Out? [d|t]: ").strip().lower()

            if choice in ("d", "dine in", "dine-in"):
                self.order_type = "Dine In"
                return
            elif choice in ("t", "take out", "take-out"):
                self.order_type = "Take Out"
                return
            else:
                print("Invalid input. Please type 'd' for Dine In or 't' for Take Out.\n")

    def get_promos(self):
        self.promos["birthday"] = self.ask_yes_no("Is it your birthday today? (15% promo)")
        self.promos["pwd_senior"] = self.ask_yes_no("Are you a PWD or Senior Citizen? (5% discount)")

    def get_subtotal(self):
        total = 0

        for info in self.items.values():
            total += info["quantity"] * info["price"]

        return total

    def get_discount_rate(self):
        rate = 0

        if self.promos["birthday"]:
            rate += 0.15

        if self.promos["pwd_senior"]:
            rate += 0.05

        return rate

    def get_discount_amount(self):
        return self.get_subtotal() * self.get_discount_rate()

    def get_total(self):
        return self.get_subtotal() - self.get_discount_amount()

    def get_print(self):
        width = 42
        subtotal = self.get_subtotal()
        discount_rate = self.get_discount_rate()
        discount_amount = self.get_discount_amount()

        print()
        print("=" * width)
        print("CEBU DE GWAPO KAINAN".center(width))
        print("=" * width)
        print(f"Order Type: {self.order_type}".center(width))
        print(datetime.datetime.now().strftime("%m/%d/%Y  %I:%M %p").center(width))
        print("-" * width)
        print(f"|{'Item':<16}|{'Qty':>4}|{'Price':>9}|{'Total':>8}|")
        print("-" * width)

        for item_name, info in self.items.items():
            quantity = info["quantity"]
            price = info["price"]
            print(f"|{item_name:<16}|{quantity:>4}|{price:>9,.2f}|{price * quantity:>8,.2f}|")

        print("-" * width)
        print(f"|{'Subtotal:':<28}{subtotal:>13,.2f}|")

        if discount_amount > 0:
            label = f"Discount ({discount_rate * 100:.0f}%):"
            print(f"|{label:<28}{-discount_amount:>13,.2f}|")

        if self.promos["birthday"]:
            print("Happy Birthday! 15% promo applied.".center(width))

        if self.promos["pwd_senior"]:
            print("PWD/Senior 5% discount applied.".center(width))

        print(f"|{'TOTAL:':<28}{self.get_total():>13,.2f}|")
        print("=" * width)
        print("Salamat po sa inyong pagbisita!".center(width))
        print("Balik po kayo ulit!".center(width))
        print("=" * width)
        print()