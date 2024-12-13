# Funkcja do opisu białka
def charakterystyka_bialka(sekwencja, masa=None, punkt_izoelektryczny=None):
    wynik = f"Długość sekwencji: {len(sekwencja)}"
    if masa:
        wynik += f", Masa: {masa} Da"
    if punkt_izoelektryczny:
        wynik += f", pI: {punkt_izoelektryczny}"
    return wynik

# Funkcja do sumowania cech białek
def sumuj_cechy_bialek(**kwargs):
    suma_mas = 0
    suma_pI = 0
    liczba_pI = 0

    for klucz, wartosc in kwargs.items():
        if "masa" in klucz:  # Sprawdza, czy klucz dotyczy masy
            suma_mas += wartosc
        elif "pI" in klucz:  # Sprawdza, czy klucz dotyczy punktu izoelektrycznego
            suma_pI += wartosc
            liczba_pI += 1

    srednia_pI = suma_pI / liczba_pI if liczba_pI > 0 else 0
    return f"Suma mas: {suma_mas} Da, Średnia pI: {srednia_pI:.2f}"
