#Funzioni   libro
def ListaCasuale(Lungh):
    s=[0]*Lungh
    for i in range(Lungh):
        import random
        s[i]=random.random()
        print(s)

def NellIntervallo(lista, limiteinferiore, limitesuperiore):
    Conteggio=0
    for Numero in lista:
        if(limiteinferiore<Numero<limitesuperiore):
            Conteggio=Conteggio+1
            print(Conteggio)

def AmpiezzaIntervallo(NumIntervalli):
    AmpiezzaIntervallo=1.0/NumIntervalli
    for i in range(NumIntervalli):
        LimiteInferiore=i*AmpiezzaIntervallo
        LimiteSuperiore=LimiteInferiore+AmpiezzaIntervallo #aggiungo al limiteinferiore una cifra fissa che corrisponde ad ampiezzaintervallo
        print("da", LimiteInferiore, "a",LimiteSuperiore)






#Lista per numeri Casuali
def CreaLista(Lungh):
    s=[0]*Lungh
    for i in range(Lungh):
        import random
        s[i]=random.random()
        if(s[Lungh-1]!=0):
            print(s)
        else:
            print("Errore di digitazione")




