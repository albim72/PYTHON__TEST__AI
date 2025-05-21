print("to jest pierwszy dokument testowy")
test:str = "to jest zmienna tekstowa"
print(test)
print(type(test))
test=66
print(test)
print(type(test))

liczba_zesp = 2+3j


print(f"liczba zespolona: {liczba_zesp}, typ: {type(liczba_zesp)}")
#typ bytes
typ_bajt = b"witaj w typie bajt!"
print(f"liczba zespolona: {typ_bajt}, typ: {type(typ_bajt)}")

#to jest komentarz
# CTRL + / -> komentowanie/odkomentowanie bloku tekstu
# CTRL + D -> powielenie bloku tekstu

"""
komentarz wieliniowy
str
dokuemntacja /pierwszy komentarz/
"""

opis = """
to jest opis programu
zmienne: a,b,c
funkcje: mcc,suma,policz
wynik: wizualizacja - wykres
"""

print(opis)
