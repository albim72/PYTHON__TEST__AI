#funkcja wyższego rzędu
def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,miejsce,punkty):
    return f"uczestnik konkursu: {imie}, miejsce: {miejsce}, liczba punktów: {punkty}"

def bonus(punkty):
    if punkty > 70:
        bn = punkty + 10
    else:
        bn = punkty
    return f'liczba punktów z bonusem: {bn}'

def osoba(funkcja,*args):
    return funkcja(*args)

def multiosoba(*args):
    b = bonus(args[2])
    konkurs(*args)
    return "opublikowane wyniki konkursu! " + b

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Ola",12,78))
print(multiosoba("Anna",21,80))

#funkcje anonimowe - lambda
def dodaj(a,b):
    return a+b

print(dodaj(2,5))

#w zamian lambda
dodaj = lambda a,b:a+b
print(dodaj(2,6))

print((lambda a,b,c:(a+b)*c)(5,2,7))

#lambda argumenty:wynik
# napisz trzy funkcje lambda które mają wykoać następujące zadania:
# podnoszenie wartości x do potęgi 5,
# od każdej wartości zadanej odejmij 1,
# połącz w jeden teskt imię i nazwisko

pt = lambda x:x**5
jeden = lambda y:y-1
osoba = lambda imie,nazwisko:f"{imie} {nazwisko}"

print(pt(6))
print(jeden(99))
print(osoba("Jan","Kot"))

#połączenie standardowych funkcji wyższego rzędu z funkcjami lambda
liczby = [1,2,4,6,7,9,12,24,57,89,90,120,121,122,134,135,136]

#potęgowanie liczb
kwadraty = list(map(lambda x:x**2,liczby))
print(kwadraty)

#wybór liczb parzystych
parzyste = list(filter(lambda x:x%2==0,liczby))

print(parzyste)

#funkcja reduce()
from functools import reduce

suma = reduce(lambda a,b:a+b,liczby)

print(suma)
print(sum(liczby))

suma2 = reduce(lambda a,b:(a+b)/3,liczby)
print(suma2)

kl = [1,]
suma3 = reduce(lambda a,b:(a+b)/3,kl)
print(suma3)

kolory = ["żółty","zielony","pomarańczowy","biały","fioletowy","czarny"]
dlugosci = list(map(lambda x:len(x),kolory))
print(dlugosci)
