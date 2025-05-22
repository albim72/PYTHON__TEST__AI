import numpy as np

print(np.__version__)

#utworzenie tablicy na podstawie listy Pythona
a = np.array([1,2,3,4,5,4])
print(f"Tablica numpy:{a}, typ: {type(a)}")

#utworzenie tablicy na podstawie listy Pythona
b = np.array([[1,2,3],[4,5,6]])
print(f"Tablica numpy:{b}, typ: {type(b)}")

print(f"element macierzy (1,2): {b[1,2]}")

lista = [[3,2],[7,3]]
print(lista[0][1])
a_p = a.reshape(2,3)
print(a_p)
c = a_p*2+b
print(c)

#iloczyn macierzowy  - mnożenie macierzy o dwolnym wymiarze A -> mxn, B -> nxp
#macierz wynikowa ma wymiar mxp

M = np.array([[1,2],[3,4],[7,9]])
N = np.array([[5,6],[7,8]])
print(f"M: {M}, N: {N}")
print(f"M*N: {np.dot(M,N)}")

#agregacje: suma,średnia,odchylenie standardowe
print(f"suma: {np.sum(M)}, średnia: {np.mean(M)}, odchylenie standardowe: {np.std(M)}")

#filtorwanie
print(f"elementy większe od 3: {M[M>3]}")

#generowanie danych
losowe = np.random.normal(loc=0.0, scale=1.0, size=5)
print(f"dane losowe (rozkład normalny): {losowe}")
