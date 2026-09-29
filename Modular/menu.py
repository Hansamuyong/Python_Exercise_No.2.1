def get_menu():
    return {
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


def display_menu(menu):
    print("=" * 42)
    print("CEBU DE GWAPO KAINAN MENU".center(42))
    print("=" * 42)
    print(f"|{'Item':<25}|{'Price':>14}|")
    print("-" * 42)

    for item, price in menu.items():
        print(f"|{item:<25}|{'P' + format(price, ',.2f'):>14}|")

    print("-" * 42)
    print()