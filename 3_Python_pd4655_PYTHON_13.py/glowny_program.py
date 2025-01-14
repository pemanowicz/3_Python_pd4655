# Glowny program
import os
import datetime
import biologia

# Tworzenie katalogu "dane_bio"
katalog = "dane_bio"
if not os.path.exists(katalog):
   os.mkdir(katalog)  
   print(f"Katalog '{katalog}' zostal utworzony.")

# przygotowanie danych
sekwencja_dna = "AGCTTAGCTAAGGCT"
wynik_nukleotydy = biologia.licz_nukleotydy(sekwencja_dna)
data_utworzenia = datetime.datetime.now()

# Tworzenie pliku i zapisanie danych 
plik_sciezka = os.path.join(katalog, "nukleotydy.txt")
with open(plik_sciezka, "w") as plik:
    plik.write("Wynik funckji licz_nukleotydy:\n")
    for nukleotyd, liczba in wynik_nukleotydy.items():
        plik.write(f"{nukleotyd}: {liczba}\n")
    plik.write(f"\nData utworzenia pliku: {data_utworzenia}\n")
print(f"Plik '{plik_sciezka}' został utworzony i zapisany.")

# Wyświetlenie wyniku funkcji opis_komorki
print(biologia.opis_komorki())