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

<<<<<<< HEAD
=======

>>>>>>> origin/master
def AmpiezzaIntervallo(NumIntervalli):
    AmpiezzaIntervallo=1.0/NumIntervalli
    for i in range(NumIntervalli):
        LimiteInferiore=i*AmpiezzaIntervallo
        LimiteSuperiore=LimiteInferiore+AmpiezzaIntervallo #aggiungo al limiteinferiore una cifra fissa che corrisponde ad ampiezzaintervallo
        print("da", LimiteInferiore, "a",LimiteSuperiore)


lista=[1,2,3,4,5,6,7,8]


NumIntervalli = 8 
Conteggio = [0] * NumIntervalli 
for i in lista: 
  Indice = int(i * NumIntervalli) 
  Conteggio[Indice] = Conteggio[Indice] + 1

<<<<<<< HEAD

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



=======
>>>>>>> origin/master

NumIntervalli = 8 
Conteggio = [0] * NumIntervalli 
AmpiezzaIntervallo = 1.0 / NumIntervalli 
for i in range(NumIntervalli): 
  LimiteInferiore = i * AmpiezzaIntervallo 
  LimiteSuperiore = LimiteInferiore + AmpiezzaIntervallo 
  Conteggio[i] = NellIntervallo(Lista, LimiteInferiore, \ 
                 LimiteSuperiore) 
print Conteggi
