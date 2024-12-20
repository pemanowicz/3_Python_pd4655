# 1 definicja zmiennych 
sekwencja_dna1 = "ATCGGCTA"
sekwencja_dna2 = "GCTAGTCA"

# 2 łączenie dwóch zmiennych
polaczona_sekwencja = sekwencja_dna1 + sekwencja_dna2
print("Polaczona sekwencja DNA:", polaczona_sekwencja)

# 3 wycinanie fragmentów za pomocą string slicing
fragment1 = polaczona_sekwencja[:8]
fragment2 = polaczona_sekwencja[4:12]
print("fragment1(pierwsze 8 nukleotydow):", fragment1)
print("fragment2(od 5. do 12. nukleotydów):", fragment2)

# 4 analiza sekwencji 
liczba_atcg = polaczona_sekwencja.count("ATCG")
pozycja_gcta = polaczona_sekwencja.find("GCTA")
print("Liczba wystapien 'ATCG':",liczba_atcg)
print("Pozycja 'GCTA':", pozycja_gcta)

# 5 Formatowanie
formatted_output = f"Sekwencja:\n\t{polaczona_sekwencja}\nFragmenty:\n\t1. {fragment1}\n\t2. {fragment2}"
print(formatted_output)


# 6 Znak ucieczki 
sekwencja_zmieniona = polaczona_sekwencja.replace("GCTA", "XXXX")  # Zamiana "GCTA" na "XXXX"
print("\nZmieniona sekwencja po zamianie 'GCTA' na 'XXXX':", sekwencja_zmieniona)