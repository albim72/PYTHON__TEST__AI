import sys

try:
    f = open("mojedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as err:
    print(f"błąd systemowy: {err}")
except ValueError:
    print(f"nie można przekonwertowac danych z typu str na int")
except Exception as exc:
    print(f"Błąd: {exc}, typ: {type(exc)}")
    print(exc.args)
except:
    print(f"nieoczekiwany błąd - {sys.exc_info()[0]}")
