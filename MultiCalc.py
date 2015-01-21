#Angolo delle funzioni
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

def NumPar(n):
    if(n%2==0):
        print("è pari")
    else:
        print("è dispari")
def Fattoriale(n):
    if(type(n)!=type(1)):
        print("il fattoriale è definito solo per i valori interi.")
        return -1
    elif(n<0):
        print("il fattoriale è definito solo per interi positivi")
        return -1
    elif(n==0):
        return 1
    else:
        return n*Fattoriale(n-1)

def CalcSconto(costo, percentuale):
    risultato=costo/100*percentuale
    print(risultato)

def Divisibile(x, y):
    if(x%y==0):
        print ("è divisibile") #x, "è divisibile per" ,y
    else:
        return ("non è divisibile") #x, "non è divisibile per", y

#Calcolatrice
operazione=0
while(operazione==0):
    #Diritti D'Autore
    print("Calcolatrice MultiUso scritta da: Andrea Toccaceli")
    print("Per i calcoli con un solo numero digitare al prima richiesta il numero che si vuole usare e alla secondo richiesta di inserimento mettere 0, per il calcolo di potenza il primo numero digitato è la base e il secondo è l esponente.")    
    #Chiedo il primo numero
    testo=input("immetti un numero: ")
    #trasformo il tetso inserito in un numero
    primo=float(testo)
    #Chiedo il secondo numero
    testo=input("Immetti un altro numero: ")
    #Trasformo il testo inserito in un numero intero
    secondo=float(testo)
    
    #Continuo a chiedere l'operazione finche non ne viene indicata una valida
    while(operazione==0):
        
        operazione=input("Scegli un operazione: \n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\n5. Fattoriale\n6. CalcSconto\n7. Divisibile\n8. NumeroPari\n9. RadiceQuadrata\n10. Potenza\n11. Fibonacci\n12. : ")
        operazione=int(operazione)
        #a seconda del ciclo selezionato saranno eseguite le istruzioni scelte
        if(operazione==1):
            risultato=primo+secondo
            print("La somma di", primo, "e", secondo,  "è", risultato)
        elif(operazione==2):
            risultato=primo-secondo
            print("La sottrazione di", primo, "e", secondo, "è", risultato)
        elif(operazione==3):
            risultato=primo*secondo
            print("La moltiplicazione di", primo, "e", secondo, "è", risultato)
        elif(operazione==4):
            risultato=primo/secondo
            print("La divisione di", primo, "e", secondo, "è", risultato)
        elif(operazione==5 and secondo==0):
            primo=int(primo)
            secondo=int(secondo)
            risultato=Fattoriale(primo)
            print("il fattoriale di", primo,  "è", risultato)
        elif(operazione==6):
            print("il primo numero immesso sarà il prezzo ed il secondo la percentuale")
            risultato=primo/100*secondo
            print("lo sconto espresso in moneta è di", risultato, "euro")
        elif(operazione==7):
            risultato=Divisibile(primo, secondo)
            print("saprai se il primo numero digitato sarà divisibile per il secondo")
            print(risultato)
        elif(operazione==8 and secondo==0):
            risultato=NumPar(primo)
            print(risultato,"se appare la scritta 'NONE' sotto il risultato è normale")
        elif(operazione==9 and secondo==0):
            import math
            risultato=math.sqrt(primo)
            print("la radice quadrata di", primo, "è", risultato)
        elif(operazione==10):
            import math
            risultato=math.pow(primo, secondo)
            print(risultato)
        elif(operazione==11 and secondo==0):
            risultato=fib(primo)
            print(risultato)
            
    #Rinizio del ciclo while
    operazione=input("\nPremi 0 per eseguire nuovamente il programma o qualunque altro numero per uscire\n: ")
    operazione=int(operazione)

print("Arrivederci Mondo!")
