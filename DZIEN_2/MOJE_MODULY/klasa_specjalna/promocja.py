from funkcja.bfunkcja import czytaj_liste,czytaj_slownik

class Filia:
    def __init__(self,nr,nazwa,adres):
        self.nr=nr
        self.nazwa=nazwa
        self.adres=adres

    def wyswietl_books(self,book):
        return f"promocja książki: {czytaj_slownik(book)}"

    def wyswietl_filia(self,flista):
        return f"nr filii: {czytaj_liste(flista)}" 
