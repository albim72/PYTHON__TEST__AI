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
