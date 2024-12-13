# Tworzenie zmiennych o różnych typach 
nazwa_genotypu = 'BRCA1' # Zmienna tekstowa (str)
liczba_mutacji = 3 # Zmienna liczby całkowitej (int)
masa_bialka = 58.44 # Zmienna liczby zmiennoprzecinkowej (float)

# Wyświetlanie typów zmiennych 
print(type(nazwa_genotypu))
print(type(liczba_mutacji))
print(type(masa_bialka))


# Wyświetlanie wartości zmiennych w jednej linii
print('Genotyp:', nazwa_genotypu, 'Liczba mutacji:', liczba_mutacji, 'Masa bialka:', masa_bialka)

# Dodawanie liczb i wyświetlanie wyniku
dodatkowe_mutacje = 2
suma_mutacji = liczba_mutacji + dodatkowe_mutacje 
print('Suma mutacji:', suma_mutacji)

# Łączenie tekstu i wyświetlanie 
opis = nazwa_genotypu + " jest ważnym genem supresorowym nowotworów."
print(opis)