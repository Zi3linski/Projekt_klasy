from obiekty.Osoba import Osoba
from typing import List
from obiekty.Przedmiot import Przedmiot


class Uczen(Osoba):
    """Klasa przechowujaca informacje o uczniach - ich przedmiotach i ocenach."""
    przedmioty = dict()

    def __init__(self,imie: str, nazwisko: str, pesel: str, wiek:int):
        super().__init__(imie, nazwisko,pesel, wiek)

    def dodajPrzedmiot(self, przedmiot: Przedmiot):
        """Dodawanie przedmiotu to listy ucznia"""
        pass

    def usunPrzedmiot(self, przedmiot: str):
        """Usuwanie przedmiotu z listy ucznia"""
        pass

    def postepy(self):
        """Zwraca ocene o postepach ucznia w nauce"""
        pass

    def dodajOcene(self, ocena: int):
        """Dodaje ocene z przedmiotu."""
        pass

    def __str__(self):
        return f"{self.imie} {self.nazwisko} lat {self.wiek}"