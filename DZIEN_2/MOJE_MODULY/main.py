# import dane
# import dane as dn
from dane import nrfilii as nf, book as bk
from funkcja.bfunkcja import czytaj_liste,czytaj_slownik
from klasa_specjalna.promocja import Filia
from matma import dodaj,mnoz
from matma.zaawansowane import potega

print(nf)
print(bk)

print("____ użycie funkcji z biblioteki bfunkcja _____")

czytaj_liste(nf)
czytaj_slownik(bk)

print("____ implementacja klasy Filia _____")
f = Filia(6,"ABC","Złota 4, Kraków")

f.wyswietl_filia(nf)
f.wyswietl_books(bk)

print("pakiet matma")
print(dodaj(2,3))
print(mnoz(5,2))
print(potega(3,2))

#instalacja lokalnie pakietu matma
#pip install -e .
