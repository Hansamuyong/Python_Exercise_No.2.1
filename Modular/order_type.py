def get_order_type():
    while True:
        choice = input("Dine In or Take Out? [d|t]: ").strip().lower()

        if choice in ("d", "dine in", "dine-in"):
            return "Dine In"
        elif choice in ("t", "take out", "take-out"):
            return "Take Out"
        else:
            print("Invalid input. Please type 'd' for Dine In or 't' for Take Out.\n")