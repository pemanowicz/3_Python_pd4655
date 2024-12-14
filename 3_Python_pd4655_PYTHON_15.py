import pandas as pd
import numpy as np

# 1 Tworzenie dataframe
dane = {
    'Gen' : ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
}

df = pd.DataFrame(dane)
print("Oryginalny DataFrame:")
print(df)

# 2 Praca z brakujacymi danymi
# spr brakujacych danych 
print("\nBrakujace dane (NaN):")
print(df.isnull())

# Usuniecie wierszy z brakujacymi danymi 
df_bez_nan = df.dropna()
print("\nDataFrame po usunieciu wierszy z brakujacymi danymi:")
print(df_bez_nan)

# uzupelnienie brakujacych danych srednimi wartoscimi w kolumnach
df_uzupelnione = df.copy()
df_uzupelnione[['Proba1', 'Proba2', 'Proba3']] = df_uzupelnione[['Proba1', 'Proba2', 'Proba3']].apply(lambda x: x.fillna(x.mean()))
print("\nDataFrame po uzupełnieniu brakujących danych średnimi wartościami:")
print(df_uzupelnione)

# 3 Operacja na danych 
# Wyciagnij dane dla genu GenA
genA = df_uzupelnione[df_uzupelnione['Gen'] == 'GenA']
print("\nDane dotyczące genu GenA:")
print(genA)

# Obliczenie sredniej ekspresji dla kazdej probki
srednia_probki = df_uzupelnione[['Proba1', 'Proba2', 'Proba3']].mean()
print("\nŚrednia ekspresja dla każdej próby:")
print(srednia_probki)

# Filtrowanie: Geny o ekspresji w probce 1 wiekszej niz 4
wysoka_ekspresja = df_uzupelnione[df_uzupelnione['Proba1'] > 4]
print("\nGeny o wysokiej ekspresji w Próbce 1 (> 4):")
print(wysoka_ekspresja)

# 4 Eksport danych do pliku CSV
plik_wynikowy = 'wynik.csv'
df_uzupelnione.to_csv(plik_wynikowy, index=False)
print(f"\nWynikowy DataFrame zapisano do pliku: {plik_wynikowy}")






