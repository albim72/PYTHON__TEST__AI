#klasa Samochod
from datetime import datetime
class Samochod:
    licznik = 0
    def __init__(self,marka,model,rocznik):
        self.marka = marka
        self.model = model
        self.rok_prod = rocznik
        Samochod.licznik += 1

    def __repr__(self):
        return f"To jest pojazd -> {self.marka}"

    def __call__(self,kolor):
        obecnyrok = datetime.now().year
        wiek = obecnyrok - self.rok_prod
        print(f"samochód {self.marka} {self.model} {kolor} z roku {self.rok_prod} ma {wiek} lat")

    def opis(self):
        return f"{self.marka} {self.model}({self.rok_prod})"

s1 = Samochod("Opel","Insignia",2017)
print(s1)
print(s1.opis())
s1("czarny")

s2 = Samochod("Jeep","Grand Cherokee",2015)
print(s2)
print(s2.opis())
s2("biały")

print(Samochod.licznik)
