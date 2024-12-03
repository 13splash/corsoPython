

# NON FUNZIONA operazioni con variabili  


print ("Pari e Dispari") 
print ("Inserisci un numero per sapere se è pari o dispari")
num = int (input())                                # num lo prende come una stringa e lo trasformo in int per operazioni algebriche
if num % 2== 0:                                                        # num è una variabile e non funziona
    print ("Il numero è pari")
else:
    print ("Il numero è dispari")                                     #INDENTAZIONE
   

"""

    commenti       
    multi
"""



print ("prova " "456")
  
print (24,465,1,100,2)                   #virgola per aggiugere
print (50+50-7)                            #operazioni algebriche
print (50+50*3)
print ("civico",123,"interno",124)


print ("inserisci nome :")                  
nomeInput = input()                       #definisco una variabile 
print("Nome ........",nomeInput)            #scrive in output il valore dato con -nomeInput- nel print



print ("Inserisci nome :")                # modello base
nome = input()
print ("Inserisci età ;")
eta = input()
print ("Questo è il tuo nome... ",nome,"         Questa è la tua età... ",eta)