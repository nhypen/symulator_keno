import random


# ===== USTAWIENIA =====
MIN_NUMBER = 1       # najmniejsza liczba w Keno
MAX_NUMBER = 70      # największa liczba w Keno (zmień na 80, jeśli chcesz)
NUM_DRAWN = 20       # ile liczb losuje Keno
DEFAULT_PLAYER_COUNT = 5  # domyślna liczba typowanych liczb


def losuj_liczby():
    """Losuje NUM_DRAWN unikalnych liczb z zakresu MIN_NUMBER–MAX_NUMBER."""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_DRAWN))


def wczytaj_liczby_gracza():
    """
    Pyta gracza o liczby.
    Możesz zatwierdzić domyślną liczbę typów (DEFAULT_PLAYER_COUNT)
    lub wpisać własną ilość.
    """
    print(f"\nIle liczb chcesz typować? [Enter = {DEFAULT_PLAYER_COUNT}]")
    wybor = input("> ").strip()

    if wybor == "":
        ile = DEFAULT_PLAYER_COUNT
    else:
        try:
            ile = int(wybor)
        except ValueError:
            print("To nie jest liczba. Używam domyślnej wartości.")
            ile = DEFAULT_PLAYER_COUNT

    if ile <= 0:
        print("Musi być co najmniej 1 liczba. Ustawiam na 1.")
        ile = 1
    if ile > NUM_DRAWN:
        print(f"Nie możesz typować więcej niż {NUM_DRAWN} liczb. Ustawiam na {NUM_DRAWN}.")
        ile = NUM_DRAWN

    print(f"\nPodaj {ile} różnych liczb z zakresu {MIN_NUMBER}-{MAX_NUMBER}:")
    liczby_gracza = set()

    while len(liczby_gracza) < ile:
        wpis = input(f"Liczba {len(liczby_gracza) + 1}: ").strip()

        try:
            n = int(wpis)
        except ValueError:
            print("To nie jest liczba, spróbuj jeszcze raz.")
            continue

        if n < MIN_NUMBER or n > MAX_NUMBER:
            print(f"Liczba musi być w zakresie {MIN_NUMBER}-{MAX_NUMBER}.")
            continue

        if n in liczby_gracza:
            print("Tę liczbę już podałaś, wybierz inną.")
            continue

        liczby_gracza.add(n)

    return sorted(liczby_gracza)


def policz_trafienia(liczby_gracza, wylosowane):
    """Zwraca listę trafionych liczb."""
    return sorted(set(liczby_gracza) & set(wylosowane))


def zagraj_raz():
    """Jedna runda gry w Keno."""
    print("\n==========================")
    print("  ISKIERKOWE SYMULATORIUM KENO")
    print("==========================")

    liczby_gracza = wczytaj_liczby_gracza()
    print(f"\nTwoje liczby: {liczby_gracza}")

    wylosowane = losuj_liczby()
    print(f"\nWylosowane liczby ({NUM_DRAWN}): {wylosowane}")

    trafione = policz_trafienia(liczby_gracza, wylosowane)

    if trafione:
        print(f"\nTrafiłaś {len(trafione)} liczb: {trafione} 🎉")
    else:
        print("\nNiestety, tym razem brak trafień. 😭")


def main():
    print("Witaj w Iskierkowym Symulatorium Keno! ⚡🎱")

    while True:
        zagraj_raz()
        print("\nZagrać jeszcze raz? [t/n]")
        odp = input("> ").strip().lower()
        if odp not in ("t", "tak", "y", "yes"):
            print("\nDzięki za grę! 💚")
            break


if __name__ == "__main__":
    main()
