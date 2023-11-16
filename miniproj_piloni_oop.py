"""
Miniproiect Piloni OOP
"""
from abc import ABC, abstractmethod
"""
1. Creaza o clasa abstracta numita Gradinita,
cu urmatoarele metode abstracte:
- activitate_practica()
- ora_de_somn()
"""
class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        pass
"""
2. Implementati doua clase, numite GradinitaPublica si
GradinitaPrivata care sa implementeze clasa abstracta Gradinita.

GradinitaPublica:
- activitate_practica() - printeaza "copiii invata sa deseneze"
- ora_de_somn() - printeaza "copiii trebuie sa doarma la ora 5"

GradinitaPrivata:
- activitate_practica() - printeaza "copiii invata sa modeleze cu plastilina"
"""
class GradinitaPublica(Gradinita):

    def __init__(self):
        self.elevi = {}

    def activitate_practica(self):
        print('Copiii invata sa deseneze')

    def ora_de_somn(self):
        print('Copii trebuie sa doarma la ora 5')

    def adauga_elevi(self, nume_elev, varsta_elev, an_inscriere):
        self.elevi[nume_elev] = {nume_elev:{"varsta": varsta_elev, "an_inscriere":an_inscriere}}
        print(self.elevi[nume_elev])

class GradinitaPrivata(Gradinita):

    def __init__(self, valoare = 5000):
        self.elevi = {}
        self.__valoare_taxa = valoare

    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina')

    def ora_de_somn(self):
        print("Copii trebuie sa doarma la ora 3")

    def adauga_elevi(self, nume_elev, varsta_elev, an_inscriere, taxa_platita):
        self.elevi[nume_elev] = {nume_elev: {"varsta": varsta_elev, "an_inscriere":an_inscriere, "taxa_platita": taxa_platita}}
        print(self.elevi[nume_elev])

    def vizualizare_elevi(self):
        for key, value in self.elevi.items():
            print(value)

    @property
    def taxa(self):
        return self.__valoare_taxa

    @taxa.getter
    def taxa(self):
        return f"Getter: Taxa este {self.__valoare_taxa} lei"

    @taxa.setter
    def taxa(self, taxa_noua):
        print("Setter:")
        if taxa_noua < 5000:
            print("Taxa este in valoare de 5000 lei. Trebuie achitata toata suma o data.")
        elif taxa_noua > 5000:
            self.__valoare_taxa = 5000
            diferenta_valoare = taxa_noua - self.__valoare_taxa
            print(f"Taxa in valoare de 5000 lei a fost platita cu succes si restul dumneavoastra este de {diferenta_valoare} lei")
        else:
            self.__valoare_taxa = taxa_noua

    @taxa.deleter
    def taxa(self):
        print(f'Deleter: Taxa a fost stearsa')
        self.__valoare_taxa = 0

"""
3.
a. Rulati codul. Se intampla ceva?
b. Instantiati un obiect din clasa GradinitaPublica si rulati codul.
Se printeaza ceva pe ecran? De ce?
c. Apelati metoda activitate_practica() si rulati codul. Ce observati?
d. Instantiati un obiect din clasa GradinitaPrivata si rulati codul.
De ce va da eroare? Cum putem rezolva eroarea?
"""
# a. Am rulat codul si nu se intampla nimic.
# b. Nu se printeaza nimic pe ecran, deoarece trebuie sa apelam o metoda
gradinita_publica = GradinitaPublica()
# c. Dupa rularea programului se va printa "Copiii invata sa deseneze"
# d. Va da erroare deoarece trebuie sa avem aceleasi metode ca si cele abstractizate din prima clasa
# Ca sa rezolvam eroare trebuie sa mai creem inca o metoda "ora_de_somn"
gradinita_privata = GradinitaPrivata()
# gradinita_privata.activitate_practica() -> va da erroare
gradinita_privata.activitate_practica() # -> dupa ce am creat si metoda "ora_de_somn"
"""
4. Creati o clasa, GradinitaPublica25, care sa mosteneasca clasa GradinitaPublica.
Implementati metoda activitate_practica() in felul urmator:
- printati mesajul "Copiii se joaca in curte pe balansoar.

- Instantiati un obiect din clasa GradinitaPublica25.
- Prin intermediul obiectului instantiat, apelati toate metodele disponibile
si observati rezultatele.
"""
class GradinitaPublica25(GradinitaPublica):

    def activitate_practica(self):
        print("Copiii se joaca in curte pe balansoar")

gradinitapublica25 = GradinitaPublica25()
gradinitapublica25.activitate_practica()
gradinitapublica25.ora_de_somn()
"""
5. Adauga un atribut pe obiect, numit elevi,
in clasele GradinitaPublica si GradinitaPrivata.
Initial, acesta va fi un dictionar gol.

Implementeaza o metoda in fiecare in aceste clase,
numita adauga_elev:

 In clasa GradinitaPublica, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>}

 In clasa GradinitaPrivata, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere, taxa_platita
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>, "taxa_platita": <taxa_platita"}

- apeleaza aceasta metoda pe un obiect din fiecare clasa pentru a ilustra
polimorfismul
"""
gradinita_publica.adauga_elevi(nume_elev="Alex",varsta_elev=14,an_inscriere=2010)
gradinita_privata.adauga_elevi(nume_elev="Dumi",varsta_elev=10,an_inscriere=2011,taxa_platita="DA")
gradinita_privata.adauga_elevi(nume_elev="Alexandru",varsta_elev=14,an_inscriere=2012,taxa_platita="NU")
"""
6. 
Adauga un atribut privat in clasa GradinitaPrivata,
numit valoare_taxa.
Creeaza o proprietate care sa incapsuleze atributul privat valoare_taxa:
- sa aiba un getter:
    - sa returneze taxa ca string cu moneda atasata ("5000 lei")
- sa aiba un setter:
    - care verifica noua taxa ce se doreste a fi platita:
    - daca e mai mica decat 5000, nu se seteaza noua taxa, si se afiseaza mesajul 
"Taxa e de 5000 lei. Trebuie achitata toata suma o data."
    - daca e mai mare de 5000, setam taxa ca fiind 5000 si afisam un mesaj
in care spunem utilizatorului ca taxa e de 5000 lei, a fost platita cu succes si
restul de bani ce ii dam inapoi.
    - daca e exact 5000, atunci setam taxa.
"""

print(gradinita_privata.taxa)
gradinita_privata.taxa = 8000

print(gradinita_privata.taxa)

del gradinita_privata.taxa

gradinita_privata.vizualizare_elevi()


