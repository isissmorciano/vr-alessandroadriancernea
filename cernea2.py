# ## Esercizio 2
# Verifica un codice alfanumerico (solo lettere e cifre) con queste regole:
# - almeno 8 caratteri;
# - primo carattere maiuscolo;
# - almeno una lettera minuscola;
# - almeno una cifra;
# - contiene solo lettere e cifre (niente spazi o caratteri speciali);
# - non deve essere nella lista `CODICI_COMUNI = ["abc12345", "student01", "prova000", "admin999"]`.

# ### Istruzioni
# Definisci le funzioni:
# - `analizza_codice(codice: str) -> dict[str, int]`: conta quante lettere maiuscole, minuscole e cifre ci sono nel codice e restituisce un dizionario con queste chiavi:
# 	- `"maiuscole"`
# 	- `"minuscole"`
# 	- `"cifre"`
  
# 	Esempio: per `Abc12346` deve restituire qualcosa come `{"maiuscole": 1, "minuscole": 2, "cifre": 5}`.
# - `valida_codice(codice: str) -> bool`: controlla se il codice rispetta tutte le regole e restituisce `True` oppure `False`. Per verificare che contenga solo lettere e cifre, puoi controllare che la somma (maiuscole + minuscole + cifre) sia uguale alla lunghezza del codice.
# - `livello_codice(codice: str) -> int`: assegna un livello da 1 a 3 in base alla lunghezza e al numero di maiuscole o cifre.

# Nel `main()`, chiedi il codice e stampa:
# - `Valido (Livello X)` se è valido;
# - `Non valido` altrimenti.

# ### Esempio
# Input: `Abc12346`

# {
#     "maiuscole": 1,
#     "minuscole": 2,
#     "cifre": 5,
# }
# Output: `Valido (Livello 2)`


def analizza_codice(codice: str) -> dict[str, int]:
    dizionario = {
            "maiuscole": 0,
            "minuscole": 0,
            "cifre": 0
        }
    for i in codice:
        for i in codice.isupper():
            dizionario["maiuscole"] += 1

def valida_codice(codice: str) -> bool:
    pass

def livello_codice(codice: str) -> int:
    livello = 0
    if codice.isupper():
        livello += 1
    
    if codice.islower():
        livello += 1

    if codice.isdigit() >= 8:
        livello += 1
    print(livello)

def main():
    print("Il codice deve essere almeno 8 caratteri")
    print("Primo carattere maiuscolo")
    print("Almeno una lettere minuscola")
    print("Almeno una cifra")
    print("Deve contenere solo lettere e cifra (niente spazi o caratteri speciali)")
    print("Non usare questi codici: 'abc12345', 'student01', 'prova000', 'admin999'")
    codice = input("Dimmi quale vuoi che sia il tuo codice?: ")
    analizza_codice(codice)
    valida_codice(codice)
    livello_codice(codice)

main()



# def analizza_codice(codice: str) -> dict[str, int]:
#     # livello = 0
#     # if codice == "abc12345":
#     #     print("scegli un altro")

#     # elif codice == "student01":
#     #     print("scegli n'altro")
#     # elif codice == "prova000":
#     #     print("SCEGLI UN ALTROO")
#     # elif codice == "admin999":
#     #     print("SCEGLI UN ALTRO CODICE.")
    
#     # if codice.isupper():
#     #     livello += 1
    
#     # if codice.islower():
#     #     livello += 1

#     # if codice.isdigit() >= 8:
#     #     livello += 1
#     # print(livello)