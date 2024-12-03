


class NomeClasse:     # creo una classe, uno scatolone 
    x=10

p1 = NomeClasse()    # oggetto , istanza della classe, creo una scatolina 

print(p1.x)             #  oggetto.  con il punto si richiama quello che c'è dentro la classe
print(NomeClasse.x)     #   classe.roba dentro la classe





#esempio di importazione modulo


from TestClasse import VisualizzaNome    #importo visualizzaNome
 
VisualizzaNome("Luca")


import random               # import modulo random che dentro ha piu funzioni
x = random.randint(1,10)    # genera un numero random da 1 a 10
VisualizzaNome(x)
