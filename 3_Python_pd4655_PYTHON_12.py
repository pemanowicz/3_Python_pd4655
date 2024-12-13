# Wlasny wyjatek dla niepraidlowej sekencji DNA
class NieprawidlowaSekwencjaDNA(Exception):
    def __init__(self, sekwencja, wiadomosc="Sekwencja zawiera nieprawidłowe znaki"):
        self.sekwencja = sekwencja
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)


# Funkcja sprawdzająca poprawność sekwencji DNA
def sprawdz_sekwencje_dna(sekwencja):
    dozwolone_nukleotydy = set("ATCG")
    if not set(sekwencja.upper()).issubset(dozwolone_nukleotydy):
        raise NieprawidlowaSekwencjaDNA(sekwencja)
    return True


# Odczyt danych z pliku
plik_wejsciowy = "sekwencje.txt"
try:
    with open(plik_wejsciowy, "r") as plik:
        zawartosc = plik.read()
        print(f"Zawartość pliku '{plik_wejsciowy}':\n{zawartosc}")
except FileNotFoundError:
    print(f"Błąd: Plik '{plik_wejsciowy}' nie istnieje.")

# Pobranie danych od użytkownika
try:
    nowa_sekwencja = input("Podaj nową sekwencję DNA (tylko litery A, T, C, G): ").strip().upper()
    sprawdz_sekwencje_dna(nowa_sekwencja)
except NieprawidlowaSekwencjaDNA as e:
    print(f"Błąd: {e.wiadomosc}. Nieprawidłowa sekwencja: {e.sekwencja}")
    exit()

# Zapis do pliku
plik_wyjsciowy = "nowa_sekwencja.txt"
with open(plik_wyjsciowy, "w") as plik:
    plik.write(nowa_sekwencja)
    print(f"Nowa sekwencja DNA została zapisana do pliku '{plik_wyjsciowy}'.")