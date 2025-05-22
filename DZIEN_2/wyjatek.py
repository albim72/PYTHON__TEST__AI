def divide_numbers():
    print("=== Kalkulator dzielenia liczb ===")
    try:
        a = float(input("Podaj liczbę (dzielna): "))
        b = float(input("Podaj liczbę (dzielnik): "))
        result = a / b
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero!")
    except ValueError:
        print("Błąd: Wprowadź poprawne liczby!")
    else:
        print(f"Wynik dzielenia: {result}")
        try:
            with open("wynik.txt", "w") as f:
                f.write(f"Wynik dzielenia: {result}\n")
        except IOError:
            print("Błąd podczas zapisu do pliku!")
        else:
            print("Wynik został zapisany do pliku.")
    finally:
        print("Dziękujemy za skorzystanie z kalkulatora.")

# Uruchomienie funkcji
divide_numbers()
