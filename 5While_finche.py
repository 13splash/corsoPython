

#while

a = 1
while a < 6:
    print(a)   
    a += 1                   # incrementare   +=        decrementare -=


"""   INFINITO
a = 1
while 1 < 6:
    print(a)   
    a += 1    
"""


import time    # importa una libreria di python

b = 10
while b <= 15:
    print(b)   
    b = b+1     
    time.sleep(1)   # intervallo di 1 secondi


    







parola = ""     # definizione variabile vuota

while parola != "stop":    # operatore bool  NON UGUALE    
    parola = input("Inserisci una parola (digita 'stop' per terminare):")
    print("fine programma")