#lista
kraje = ["Polska","Portugalia","USA","Niemcy","Egipt","Polska","Szwecja","Boliwia"]
print(kraje)
print(type(kraje))
print(kraje[0])
print(kraje[4])
print(kraje[1:5])
print(kraje[:3])
print(kraje[2:])
print(kraje[-1])
#iteracyjność
print("kraje z listy\n______________________\n")
for k in kraje:
    print(k)

kraje.append("Japonia")
print(kraje)

kraje.insert(1,"RPA")
print(kraje)

kraje.sort()
print(kraje)


kraje.sort(reverse=True)
print(kraje)

kraje.remove("Szwecja")
print(kraje)

kraje.remove("Polska")
print(kraje)

del kraje[6]
print(kraje)

mieszana = [35,7.75,"Toruń",3,-11,0.45,True,b'takie tam']
print(mieszana)

inside = [3,2,53,[4.4,4,3.64,1],True,7,[True,False,True,[6,3,67]]]
print(inside)
print(inside[6][3][1])

#krotka(tuple)
animal = ("pies","kot","papuga","koń","szczur","kot","hipopotam")
print(animal)
print(type(animal))
print(animal.count("kot"))

if "papuga" in animal:
    print("Tak! to działa")

print("koń" in animal)

kolory = ("czerwony","zielony","biały",)
print(kolory)
print(type(kolory))

aniaml_l = list(animal)
print(aniaml_l)
aniaml_l.append("sokół")
animal = tuple(aniaml_l)

print(animal)

#zbiory
drzewa = {"dąb","sosna","topola","brzoza","dąb","dąb","jodła"}
print(drzewa)
print(drzewa)
print(drzewa)

drzewa.add("osika")
print(drzewa)

ekstra = ["świerk","jabłoń","cyprys"]
drzewa.update(ekstra)
print(drzewa)

drzewa.remove("topola")
print(drzewa)

#słownik - dictionary
pojazd = {
    "marka":"Ford",
    "model":"Mustang",
    "rok":2010,
    "kolor":"czarny",
    10004:"pb98"
}

print(pojazd)
print(type(pojazd))

print(pojazd["model"])

miasto = {
    "Warszawa":{
        "województwo":"mazowieckie",
        "populacja":1890340,
        "powierzchnia":517.4
    },
    "Kraków":{
        "województwo":"małopolskie",
        "populacja":780000,
        "powierzchnia":326.86
    },
    "Łódź":{
        "województwo":"łódzkie",
        "populacja":670100,
        "powierzchnia":293.25
    },
    "Wrocław":{
        "województwo":"dolnośląskie",
        "populacja":643782,
        "powierzchnia":293.85
    },
    "Gdańsk":{
        "województwo":"pomorskie",
        "populacja":470900,
        "powierzchnia":262
    }
}

