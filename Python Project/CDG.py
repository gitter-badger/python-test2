#Calcolatore Di Giorni
operazione=0
while(operazione==0):
    #Chiedo di inserire le ore
    ore=input("Inserisci le ore: ")
    #trasformo il testo inserito in un numero
    ore=int(ore)
    
    #Continuo a chiedere l'operazione finche non ne viene indicata una valida
    while(operazione==0):
        operazione=input("che operazione desideri eseguire?\n1. Giorni\n2. :  ")
        operazione=int(operazione)
        
        if(operazione==1):
            risultato=ore/24
        else:
            operazione=0
            #messaggio d'errore
            print("\nSelezionare un operazione valida!\n")
            
     #Scrivo il risultato
    print("risulato= %d" %(risultato))
