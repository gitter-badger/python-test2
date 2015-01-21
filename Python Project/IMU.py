#Calcolatrice
operazione=0
while(operazione==0):
    #Chiedo il primo numero
    primo=input("immetti un numero: ")
    #trasformo il tetso inserito in un numero
    primo=int(primo)
    #Chiedo il secondo numero
    secondo=input("Immetti un altro numero: ")
    #Trasformo il testo inserito in un numero intero
    secondo=int(secondo)
    #Chiedo il terzo numero
    terzo=input("Immetti un altro numero: ")
    #Trasformo il numero in decimale
    terzo=int(terzo)
    
    #Continuo a chiedere l'operazione finche non ne viene indicata una valida
    while(operazione==0):
        operazione=input("che operazione desideri eseguire?\n1. IMU\n2. : ")
        
        operazione=int(operazione)
        
        if(operazione==1):
            number=[(primo*secondo*terzo)/1000*10]*10/60
        
        
        
        
        else:
            operazione=0
            #messaggio d'errore
            print("\nSelezionare un operazione valida!\n")
            
        
    #Scrivo il risultato
    print("number= %d" %(number))
    operazione=input("\nPremi 0 per eseguire nuovamente il codice o qualunque altro numero per uscire\n: ")
    operazione=int(operazione)
    
print("Arrivederci")

    
