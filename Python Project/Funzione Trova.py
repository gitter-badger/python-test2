def Trova(Stringa,Carattere, Posizione):
    Indice=Posizione
    while(Indice<len(Stringa)):
        if(Stringa[Indice]==Carattere):
            print(Indice)
            Indice=Indice+1
    return(-1)
    
Trova("banana","a", 1)
