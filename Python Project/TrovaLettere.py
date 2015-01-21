
vocali=["a","e","i","o","u"]
consonanti=["b","c","d","f","g","h","l","m","n","p","q","r","s","t","u","v","z"]
def TrovaLettere(Parola, vocali, Posizione):
    vocali=["a","e","i","o","u"]
    i=1
    for lettere in Parola[Posizione:]:
        if(lettere[Posizione:]==vocali):
            print(i)
            i=i+1
   
TrovaLettere("banana", vocali, 1)
    
