# ## Esercizio 1
# Chiedi quanti numeri inserire (`n > 0`), leggi i numeri e salvali in una lista.

# Il programma deve:
# - creare una lista con i numeri positivi e pari;
# - contare i numeri dispari negativi;
# - calcolare la media assoluta dei numeri;
# - stampare lista inserita, lista filtrata, conteggio e media.

# ### Esempio
# Input: `2, -3, 4, -5, 6`

# Output:
# - `Lista inserita: [2, -3, 4, -5, 6]`
# - `Positivi pari: [2, 4, 6]`
# - `Conteggio dispari negativi: 2`
# - `Media assoluta: 4.0`

# ---

lista_numeri: list = []
lista_positiva: int = []
lista_negativa: int = []
negativita = 0

chiedere1: int = int(input("Quanti numeri vuoi inserire?: "))
if chiedere1 < 0:
    print("Devi darmi un numero positivo ed intero.")

for i in range(chiedere1):
    numeretto: int = int(input("Dimmi il numero: "))
    lista_numeri.append(numeretto)
    if numeretto % 2 == 0 and numeretto > 1:
        lista_positiva.append(numeretto)
    elif numeretto % 2 == 1 and numeretto < 1:
        negativita += 1

for i in range(chiedere1):
    media = abs(sum(lista_numeri)) / abs(len(lista_numeri))

print(f"Lista inserita: {lista_numeri}")
print(f"Positivi pari: {lista_positiva}")
print(f"Conteggio dispari negativi: {negativita}")
print(f"Media assoluta: {media:}")