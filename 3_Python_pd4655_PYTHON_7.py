# 1 Zadeklarowanie zmiennych typu boolean
czy_sekwencja_dna_aktywna = True
czy_mutacja_punktowa = False

print(f"Czy sekwencja DNA aktywna? {czy_sekwencja_dna_aktywna}")
print(f"Czy mutacja punktowa? {czy_mutacja_punktowa}")


# 2 Sprawdzanie zmiennych z użyciem funkcji bool()
ciag_znakow = "ATCG"
pusta_lista = []
liczba = 0

print(f"Czy ciąg znaków nie jest pusty? {bool(ciag_znakow)}")
print(f"Czy lista jest pusta? {bool(pusta_lista)}") 
print(f"Czy liczba jest różna od zera? {bool(liczba)}")


# 3 Operacje arytmetyczne
liczba_nukleotydow = 256  
liczba_kodonow = liczba_nukleotydow // 3  
reszta_nukleotydow = liczba_nukleotydow % 3

print(f"Liczba kodonów: {liczba_kodonow}")
print(f"Reszta nukleotydów: {reszta_nukleotydow}")

suma = liczba_nukleotydow + 44
roznica = liczba_nukleotydow - 100
iloczyn = liczba_nukleotydow * 2

print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")


# 4 Operatory przypisania
liczba_nukleotydow += 44 
liczba_nukleotydow -= 100  
print(f"Aktualna liczba nukleotydów: {liczba_nukleotydow}")


# 5 Operatory porównania
dlugosc_sekwencji1 = 200
dlugosc_sekwencji2 = 200

if dlugosc_sekwencji1 < dlugosc_sekwencji2:
    print("Sekwencja 2 jest dłuższa od sekwencji 1")
elif dlugosc_sekwencji1 > dlugosc_sekwencji2:
    print(f"Sekwencja 1 jest dłuższa od sekwencji 2")
else:
    print(f"Obie sekwencje mają taką samą długość")
