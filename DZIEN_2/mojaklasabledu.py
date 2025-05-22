class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołanie funkcji __str__")
        if self.message:
            return f'{self.__class__.__name__}: {self.message}'
        else:
            return f'{self.__class__.__name__}: brak informacji'

n = input("podaj literę alfabetu (a-z) -> ")
try:
    if n=="a" or n == "123":
        raise MojaKlasaBledu(f"{n} jest zarezerwowane")
    else:
        print("dzień dobry!")
except MojaKlasaBledu as mc:
    print(mc)
