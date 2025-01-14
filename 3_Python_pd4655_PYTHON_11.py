# Utworz klasę organizm 
class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj


    def opisz(self):
        return f"Organizm: {self.nazwa}, Rodzaj: {self.rodzaj}"

    @staticmethod
    def transkrybuj(sekwencja_dna):
        return sekwencja_dna.replace("T", "U")


# Klasa bakteria, która odziedziczy po klasie organizm
class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, kształt):
        super().__init__(nazwa, rodzaj)
        self.kształt = kształt

    def opisz(self):
        opis_organizm = super().opisz()
        return f"{opis_organizm}, Kształt: {self.kształt}"

bakteria1 = Bakteria("Escherichia coli", "Prokariot", "Pałeczkowaty")
bakteria2 = Bakteria("Staphylococcus aureus", "Prokariot", "Kulisty")
bakteria3 = Bakteria("Bacillus subtilis", "Prokariot", "Laseczkowaty")

print(bakteria1.opisz())
print(bakteria2.opisz())
print(bakteria3.opisz())


sekwencja_dna = "ATGCTAGCTAGCTTAA"
sekwencja_rna = Organizm.transkrybuj(sekwencja_dna)
print(f"Sekwencja RNA: {sekwencja_rna}")