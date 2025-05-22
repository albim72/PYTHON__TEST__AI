from abc import ABC, abstractmethod

# === KLASA ABSTRAKCYJNA ===
# Służy jako "szkielet" – nie można jej stworzyć bezpośrednio, tylko odziedziczyć.
class Zwierze(ABC):
    def __init__(self, imie):
        self._imie = imie  # ENKAPSULACJA: zmienna z podkreśleniem sugeruje prywatność

    @abstractmethod
    def daj_glos(self):
        pass  # KAŻDA klasa dziedzicząca musi zaimplementować tę metodę


# === POLIMORFIZM I DZIEDZICZENIE ===
class Pies(Zwierze):
    def __init__(self, imie, rasa):
        super().__init__(imie)  # Dziedziczenie konstruktora z klasy bazowej
        self.rasa = rasa

    def daj_glos(self):
        return "Hau hau!"

    def aportuj(self):
        return f"{self._imie} aportuje patyk."


class Kot(Zwierze):
    def __init__(self, imie, kolor):
        super().__init__(imie)
        self.kolor = kolor

    def daj_glos(self):
        return "Miau miau!"

    def drap(self):
        return f"{self._imie} drapie kanapę."


# === PROPERTY: sposób dostępu do pól prywatnych ===
class Czlowiek:
    def __init__(self, imie, wiek):
        self._imie = imie
        self._wiek = wiek

    @property
    def imie(self):
        return self._imie

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        if nowy_wiek > 0:
            self._wiek = nowy_wiek
        else:
            raise ValueError("Wiek musi być dodatni")


# === __new__ i __init__ ===
# __new__ tworzy instancję (mało używane, np. przy singletonach), __init__ ją inicjalizuje
class Jednorozec:
    def __new__(cls, *args, **kwargs):
        print("[__new__] Tworzenie magicznego jednorożca...")
        return super().__new__(cls)

    def __init__(self, kolor):
        print("[__init__] Inicjalizacja jednorożca")
        self.kolor = kolor

    def __str__(self):
        return f"Jednorożec w kolorze {self.kolor}"


# === __call__: obiekt staje się funkcją ===
class Licznik:
    def __init__(self):
        self._liczba = 0

    def __call__(self):
        self._liczba += 1
        print(f"Obiekt wywołany {self._liczba} razy")


# === __iter__: obiekt staje się iterowalny ===
class LiczbyDo:
    def __init__(self, max_liczba):
        self.max = max_liczba

    def __iter__(self):
        self._aktualna = 0
        return self

    def __next__(self):
        if self._aktualna < self.max:
            self._aktualna += 1
            return self._aktualna
        else:
            raise StopIteration


# === PRZYKŁADOWE ZASTOSOWANIE ===
if __name__ == "__main__":
    # Polimorfizm: różne zwierzęta, to samo API
    zwierzaki = [
        Pies("Reksio", "bulldog"),
        Kot("Mruczek", "czarny")
    ]

    for zwierzak in zwierzaki:
        print(f"{zwierzak._imie} mówi: {zwierzak.daj_glos()}")

    # Property
    jan = Czlowiek("Jan", 40)
    print(f"{jan.imie} ma {jan.wiek} lat.")
    jan.wiek = 41

    # __new__ i __init__
    j = Jednorozec("tęczowy")
    print(j)

    # __call__
    licznik = Licznik()
    licznik()
    licznik()

    # __iter__
    print("Iteracja po LiczbyDo(5):")
    for liczba in LiczbyDo(5):
        print(liczba)
