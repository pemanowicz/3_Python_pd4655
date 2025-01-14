import numpy as np

# tworzenie macierzy dla ekspresji genow 
macierz_ekspresji = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])


print("Oryginalna macierz ekspresji:")
print(macierz_ekspresji)

# 2 Zwiekszenie ekspresje wszystkich genow o 5%
macierz_zmieniona = macierz_ekspresji * 1.05
print("\nMacierz po zwiększeniu ekspresji o 5%:")
print(macierz_zmieniona)

# 3 Obliczenie sredniej kespresji dla kazdego genu
srednia_genow = np.mean(macierz_zmieniona, axis=1)
print("\nŚrednia ekspresja dla każdego genu:")
print(srednia_genow)

# 4 Obliczam sume ekspresji genow dla kazdej proby
suma_prob = np.sum(macierz_zmieniona, axis=0)
print("\nsuma ekspresji genow dla kazdej proby:")
print(suma_prob)

# 5 wprowadzenie wartosi Nan  dla kilku prob 
macierz_zmieniona[0, 1] = np.nan  # Pierwszy gen, druga próba
macierz_zmieniona[2, 2] = np.nan  # Trzeci gen, trzecia próba
print("\nMacierz z brakującymi danymi (NaN):")
print(macierz_zmieniona)

# 6 Obliczenie średniej ekspresji genów ignorując NaN
srednia_bez_nan = np.nanmean(macierz_zmieniona, axis=1)
print("\nŚrednia ekspresja genów z pominięciem brakujących danych:")
print(srednia_bez_nan)