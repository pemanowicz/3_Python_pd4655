# 1. Zdefiniowanie zmiennej przechowującej sekwencję DNA jako string 
sekwencja_dna = "ATCGGCTA" # Zmienna tekstowa przechowująca sekwencję DNA 

# 2. Wyświetlenie wartości zmiennej i jej typu w jednej linijce 
print("Wartosc zmiennej:", sekwencja_dna, "typ zmiennej:", type(sekwencja_dna))

# 3. Konwersja zmiennej na listę (list)
sekwencja_dna_lista = list(sekwencja_dna)

# 4. Ponowne wyświetlenie wartości zmiennej i jej typu 
print("Wartosc po konwersji:", sekwencja_dna_lista, "Typ zmiennej:", type(sekwencja_dna_lista))

# 5. Użycie funkcji range do generowania indeksów sekwencji DNA
for i in range(len(sekwencja_dna_lista)):
	print(f"Indeks: {i} Nukleotyd: {sekwencja_dna_lista[i]}")