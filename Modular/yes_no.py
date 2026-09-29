def ask_yes_no(question):
    while True:
        answer = input(question + " [yes|no]: ").strip().lower()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.\n")