def czytaj_liste(lista):
    print(f"________ lista: {lista} __________")
    for i,j in enumerate(lista):
        print(f"element listy {i+1} -> wartość {j}")
        
def czyta_slownik(s):
    print(f"________ slownik: {s} __________")
    for i,j in s.items():
        print(f"element slownika {i} -> wartość {j}")
