import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dane
proby = ['Proba1', 'Proba2', 'Proba3']
geny = ['GenA', 'GenB', 'GenC']
ekspresja = np.array([
    [5.1, 2.3, 7.8],  # Ekspresja GenA
    [3.2, 4.5, 6.1],  # Ekspresja GenB
    [4.8, 5.5, 3.9]   # Ekspresja GenC
])

# wykres liniowy
plt.figure(figsize=(8,5))
for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)
plt.title("Wykres liniowy ekspresji genów w próbkach")
plt.xlabel("Próbki")
plt.ylabel("Ekspresja")
plt.legend(title="Geny")
plt.grid(True)
plt.show()

# wykres slupkowy
x = np.arange(len(proby))  
width = 0.25

for i, gen in enumerate(geny): 
    plt.bar(x + i * width, ekspresja[i], width, label=gen)

plt.xticks(x + width, proby)
plt.title("Wykres słupkowy ekspresji genów")
plt.xlabel("Próbki")
plt.ylabel("Ekspresja")
plt.legend(title="Geny")
plt.grid(True)
plt.show()

# Wykres rozrzutu
plt.figure(figsize=(8, 5))
plt.scatter(ekspresja[0], ekspresja[1], color='green', marker='x')
plt.title("Wykres rozrzutu GenA vs GenB")
plt.xlabel("Ekspresja GenA")
plt.ylabel("Ekspresja GenB")
plt.grid(True)
plt.show()

# Violin plot
plt.figure(figsize=(8, 5))
sns.violinplot(data=ekspresja.T, palette="Set2")
plt.xticks(ticks=np.arange(len(geny)), labels=geny)
plt.title("Violin plot ekspresji genów")
plt.xlabel("Geny")
plt.ylabel("Ekspresja")
plt.show()

# Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=ekspresja.T, palette="Set3")
plt.xticks(ticks=np.arange(len(geny)), labels=geny)
plt.title("Box plot ekspresji genów")
plt.xlabel("Geny")
plt.ylabel("Ekspresja")
plt.savefig("ekspresja_genow.png")
plt.show()

print("Wykres pudełkowy zapisano do pliku 'ekspresja_genow.png'.")
