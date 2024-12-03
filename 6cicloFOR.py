
# CICLO FOR
                            # i (indice)(posizione)  variabile..  che va da 1 a 11 ..print
for i in range(0,5):       #scrive i numeri da 1 a 10
    print(i)




nomi = ["ALI", "bob", "jack"]
for nomi in nomi:
    print(f"Ciao, {nomi}!")       # f serve per scrivere {variabile stampata a schermo}




listaNum = [1, 2, 3, 4, 5]
somma = 0
for numero in listaNum:
    somma  += numero
print("La somma è:", somma)       # importante INDENTAZIONE , se fosse nel ciclo for l'output sarebbe diverso



parola = "Python"                # anche con le parole
for carattere in parola:
    print(carattere)
#print(carattere)




frutti = {"mela": "rossa", "banana": "gialla", "uva": "viola"}            #dizionario    chiace : valore , chiave : valore
for frutto, colore in frutti.items():         #items() per dizionari
    print("La "+frutto+" è "+colore+".")




