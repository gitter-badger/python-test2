#Prova 1 Funzione
def ContoAllaRovescia(n):
    if(n>0):
        print(n, "oooooooo")
        ContoAllaRovescia(n-1)
    if(n==0):
        print("yeeehhhh!")
n=input("Digita un numero per il conto alla rovescia: ")
n=int(n)
secondo=ContoAllaRovescia(n)
#Prova 2 Funzione
testo01=input("Bene... Ed Ora digita un altro numero per lasciare alcune righe vuote: ")
def NRigaVuota(n):
    
    if(n>0):
        print()
        NRigaVuota(n-1)
    if(n==0):
        print("Magia, puf!")
terzo=NRigaVuota(n)

#Prova 3 Funzione
testo02=input("Ti stai divertendo?... Digita un altro numero e scoprirai se il tuo  humero è pario o qualcosaltro: ")
def NP(n):
    if(n%2==0):
        print("Mh Ottimo.. QUESTO NUMERO è PARI")
    elif(n%2==1):
        print("Questo numero da resto 1, il calcolo non riporta le cifre mobili")
    elif(n%3==0):
        print("Questo Numero è un multiplo di 3 e non di 2")
    elif(n%2!=0):
            print("Questo Numero da un resto superiore ad 1")
quarto=NP(n)

#Funzione Finale
testo03=0
while(testo03==0):
    testo03=input("Ricapitolando.. Quale funzione ti è piaciuta di più?\n1. Funzione1\n2. Funzione2\n3. Funzione3\n3.")
    
        if(testo03==1):
            print("La tua preferità è il ContoAllaRovescia")
       
        elif(testo03==2):
            print("Mh ti piace questa, Le righe vuote")
        
        elif(testo03==3):
            print("La tua preferita è questa, I numeri pari")
        
