# uttwórz listę i krotkę
lista_nukleotydow = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
krotka_zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')

# druk pierwszy i ostatni element listy oraz krotki
print(f"Pierwszy element listy: {lista_nukleotydow[0]}")
print(f"Ostatni element listy: {lista_nukleotydow[-1]}")
print(f"Pierwszy element krotki: {krotka_zasady_azotowe[0]}")
print(f"Ostatni element krotki: {krotka_zasady_azotowe[-1]}")

# odyfikacje
lista_nukleotydow.pop(2)
lista_nukleotydow.append('U')
print(f"Zmodyfikowana lista: {lista_nukleotydow}")

# Dodanie elementu na koncu listy
lista_nukleotydow.append('C')
print(f"Lista po dodaniu elementu: {lista_nukleotydow}")

# Przejdz przez wszystkie elementy listy i krotki
print("Elementy listy:")
for nukleotyd in lista_nukleotydow:
	print(nukleotyd)

print("Elementy krotki:")
for zasada in krotka_zasady_azotowe:
	print(zasada)

# list comprehension 
nowa_lista = [element.lower() for element in lista_nukleotydow]
print(f"Nowa lista z małymi literami: {nowa_lista}")
