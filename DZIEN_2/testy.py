import unittest
from opowiesc_o_obiektowosci import Pies, Kot, Czlowiek, Jednorozec, Licznik, LiczbyDo


class TestZwierze(unittest.TestCase):
    def test_pies_daje_glos(self):
        pies = Pies("Burek", "mieszaniec")
        self.assertEqual(pies.daj_glos(), "Hau hau!")
        self.assertIn("aportuje", pies.aportuj())

    def test_kot_daje_glos(self):
        kot = Kot("Filemon", "biały")
        self.assertEqual(kot.daj_glos(), "Miau miau!")
        self.assertIn("drapie", kot.drap())


class TestCzlowiek(unittest.TestCase):
    def test_property_wiek(self):
        osoba = Czlowiek("Anna", 30)
        self.assertEqual(osoba.imie, "Anna")
        self.assertEqual(osoba.wiek, 30)

        osoba.wiek = 35
        self.assertEqual(osoba.wiek, 35)

    def test_bledny_wiek(self):
        osoba = Czlowiek("Ewa", 25)
        with self.assertRaises(ValueError):
            osoba.wiek = -10


class TestJednorozec(unittest.TestCase):
    def test_kolor_jednorozca(self):
        j = Jednorozec("srebrny")
        self.assertEqual(j.kolor, "srebrny")
        self.assertIn("srebrny", str(j))


class TestLicznik(unittest.TestCase):
    def test_call(self):
        licznik = Licznik()
        licznik()
        licznik()
        self.assertEqual(licznik._liczba, 2)


class TestLiczbyDo(unittest.TestCase):
    def test_iteracja(self):
        liczby = list(LiczbyDo(3))
        self.assertEqual(liczby, [1, 2, 3])

    def test_pusta_iteracja(self):
        liczby = list(LiczbyDo(0))
        self.assertEqual(liczby, [])


if __name__ == '__main__':
    unittest.main()
