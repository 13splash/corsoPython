

                                #INTRODUZIONE DI ELIF   
numero = 0                     #  IF  ELSE ELIF

if numero > 0:
    print("Il numero è positivo")
elif numero < 0:                        # ELIF    Else if
    print("Il numero è negativo")
else:
    print("Il numero è zero")




print("INSERISCI PASSWORD SICURA")
password = input()                               # controllo condizionale di una stringa

if password == "passwordSicura":
    print("Accesso consentito")
else:
    print("Accesso negato")