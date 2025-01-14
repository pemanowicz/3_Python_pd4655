# zmiennee o różnych typach 
nazwa_genotypu = 'BRCA1' (str)
liczba_mutacji = 3 (int)
masa_bialka = 58.44 (float)

# wyświetlanie typów zmiennych 
print(type(nazwa_genotypu))
print(type(liczba_mutacji))
print(type(masa_bialka))


# wyświetlanie wartości zmiennych w jednej linii
print('Genotyp:', nazwa_genotypu, 'Liczba mutacji:', liczba_mutacji, 'Masa bialka:', masa_bialka)

# Dodawanie liczb i wyświetlanie wyniku
dodatkowe_mutacje = 2
suma_mutacji = liczba_mutacji + dodatkowe_mutacje 
print('Suma mutacji:', suma_mutacji)

# lączenie tekstu i wyświetlanie 
opis = nazwa_genotypu + " jest ważnym genem supresorowym nowotworów."
print(opis)