#funkcja czysta
import time


def pole_prostokata(a,b):
    return a*b


#funkcja nieczysta
def pole_prostokata_n(a,b):
    wynik = a*b
    print(wynik)
    return wynik

print(pole_prostokata(3,5))
print(pole_prostokata_n(2,7))

#funkcja zmieniająca stan globalny
lista = [2,4,7,8,3]
def dodaj_element(x):
    lista.append(x)

dodaj_element(6)
print(lista)

#przykłady funkcji które zwaracją różne wyniki dla tych samych parametrów
#1 - użycie losowości
import random

def losowy_bonus(punkty):
    return punkty + random.randint(1,10)

print(losowy_bonus(100))
print(losowy_bonus(100))

#2 - użycie czasu
from datetime import datetime

def czas_powitania(imie):
    teraz = datetime.now().strftime("%H:%M:%S.%f")
    time.sleep(1)
    return f"Cześć {imie}, jest godzina: " + teraz

print(czas_powitania("Ala"))
print(czas_powitania("Olaf"))
print(czas_powitania("Renata"))

#3 - zależność od zmiennej globalnej
licznik = 0
def dodaj_i_zlicz(x):
    global licznik
    licznik += 1
    return x + licznik

print(dodaj_i_zlicz(5))
print(dodaj_i_zlicz(5))

#funkcje za parametrami domyślnymi

#1
def przywitaj(imie="Janusz"):
    print(f"Cześć, {imie}!")

przywitaj("Ola")
przywitaj()

#przykład niebezpieczny!
def dodaj_wartosc(x,lista=[]):
    lista.append(x)
    return lista

print(dodaj_wartosc(1))
print(dodaj_wartosc(2))

#wersja poprawna
def dodaj_dobrze(x,lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista

print(dodaj_dobrze(1))
print(dodaj_dobrze(2))

#funkcja z zależnymi parametrami domyślnymi
def przydziel_bonus(punkty,mnoznik=1.1):
    return punkty*mnoznik

print(przydziel_bonus(45))
print(przydziel_bonus(45,1.2))

#prametr domyślny jako funkcja(callback)
def opercja(x,y,metoda=lambda a,b:a+b):
    return metoda(x,y)

print(opercja(3,4))
print(opercja(3,4,lambda a,b:40*a*b))
