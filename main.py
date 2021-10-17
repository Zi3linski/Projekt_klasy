

from obiekty.Uczen import Uczen
from obiekty.Przedmiot import Przedmiot
from obiekty.Uczen import Uczen
from string import digits, ascii_letters
def main():
    p1=Przedmiot("Polski",1,35,"Pt",12)
    p1.dodajOcene(5)
    p1.dodajOcene(4)
    print(p1)
    p1.usun_ocene(4)
    print(p1)

    u1=Uczen("Michal","Zieliński","7587934245",25)
    u1.dodajPrzedmiot(p1)
    u1.dodajOcene("Polski",5)
    u1.dodajOcene("Polski",1)
    u1.dodajOcene("Polski",4)
    u1.dodajPrzedmiot(Przedmiot("Matematyka",2,35,"Wt",2))
    print(u1.postepy("Polski"))

    u1.pokazPrzedmiot("Polski")
    u1.usunPrzedmiot("Matematyka")

    u1.pokazPrzedmiot("Matematyka")
    # uczen = Uczen("Michal", "Zielinski", "879878979879", 30)
    # print(uczen)
    # print(ascii_letters)

if __name__ == '__main__':
    main()


