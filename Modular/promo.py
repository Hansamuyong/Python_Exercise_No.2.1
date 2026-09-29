from yes_no import ask_yes_no


def get_promos():
    promos = {}

    promos["birthday"] = ask_yes_no("Is it your birthday today? (15% promo)")
    promos["pwd_senior"] = ask_yes_no("Are you a PWD or Senior Citizen? (5% discount)")

    return promos