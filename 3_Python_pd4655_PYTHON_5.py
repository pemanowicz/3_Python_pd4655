# definiowanie zmiennej ako string 
sekwencja_dna = "ATCGGCTA"
# wyświetlenie wartości zmiennej i jej typu w jednej linijce 
print("Wartosc zmiennej:", sekwencja_dna, "typ zmiennej:", type(sekwencja_dna))

# konwersja zmiennej na listę (list)
sekwencja_dna_lista = list(sekwencja_dna)

# ponowne wyświetlenie wartości zmiennej i jej typu 
print("Wartosc po konwersji:", sekwencja_dna_lista, "Typ zmiennej:", type(sekwencja_dna_lista))

# użycie funkcji range do generowania indeksów sekwencji DNA
for i in range(len(sekwencja_dna_lista)):
	print(f"Indeks: {i} Nukleotyd: {sekwencja_dna_lista[i]}")