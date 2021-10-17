from typing import List
from dataclasses import dataclass,field

@dataclass
class Przedmiot:
    nazwa: str
    oceny: List[int] = field(init=False)
    iloscGodzin: int
    cena: int
    dzientygodnia: str
    godzina: int

    def __post_init__(self):
        """Tworzenie ustej listy ocen"""
        self.oceny=list()

    def __str__(self):
        return f"Przedmiot: {self.nazwa},ilosc godzin:{self.iloscGodzin}" \
               f",cena za godzine:{self.cena} zł, dzien:{self.dzientygodnia}, o godzinie{self.godzina}" \
               f",oceny z przedmiotu{self.oceny if len(self.oceny)>0 else 'Brak ocen'}"

    def dodajOcene(self,ocena:int) -> None:
        """Dodawanie nowej oceny z przedmiotu"""
        self.oceny.append(ocena)

    def usun_ocene(self,ocena:int)->None:
        self.oceny.remove(ocena)

    def srednia(self) -> float:
        suma=0
        for i in self.oceny:
            suma+=i
        return suma/len(self.oceny)
