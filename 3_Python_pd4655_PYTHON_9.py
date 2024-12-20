# zbiór i slownik z uniklanymi elementami
zbior_nukleotydow = {"A", "T", "G", "C"}
slownik_geny = {
	"BRCA1": "naprawa NDA",
	"TP53": "regulacja cyklu komórkowego",
	"EGFR": "sygnalizacja wzrostu",
}

# Dodanie nowego elementu do zbioru 
zbior_nukleotydow.add("U") 
slownik_geny["MYC"] = "regulacja transkrypcji"

# 3 Spr czy dany element istnieje w zbiorze i slowniku
print("Czy 'A' istnieje w zbiorze nukleotydow?", "A" in zbior_nukleotydow)
print("Czy 'BRCA1' jest kluczem w slowniku genow?", "BRCA1" in slownik_geny)

# 4 Usuniecie jednego element zbioru 
zbior_nukleotydow.discard("G")
print(f"Zbior nukleotydow po usunieciu elementu 'G':", zbior_nukleotydow)

# 5 Wyswietlenie zawartosc slownika: klucze i wartosci za pomoca petli for 
print("Zawartosc slownika geny:")
for klucz, wartosc in slownik_geny.items():
	print(f"Gen: {klucz}, Funkcja: {wartosc}")

# 6 Sprawdz dlugosc zbioru za pomoca instrukcji warunkowej 
if len(zbior_nukleotydow) > 3:
	print("Zbior nukleotydow ma wiecej niz 3 elementy")
else: 
	print("Zbior nukleotydow ma 3 lub mniej elementow")

# 7 Spr czy okreslony klucz istnieje w slowniku i wyswietlam jego wartosc
if "TP53" in slownik_geny:
	print(f"Funckja genu 'TP53': {slownik_geny['TP53']}")
else:
	print("Gen 'TP53' nie istnieje w slowniku")

# 8 Laczenie zbiorow i wydruk wyniku
inny_zbior_nukleotydow = {"X", "Y", "Z"}
wynik_union = zbior_nukleotydow.union(inny_zbior_nukleotydow)
print("Polaczony zbior nukleotydow:", wynik_union)