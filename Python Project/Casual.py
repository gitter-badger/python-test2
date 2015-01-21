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


def AmpiezaIntervallo(NumIntervalli):
    AmpiezzaIntervallo=1.0/NumIntervalli
    for i in range(NumIntervalli):
        LimiteInferiore=i*AmpiezzaIntervallo
        LimiteSuperiore=LimiteInferiore+AmpiezzaIntervallo #aggiungo al limiteinferiore una cifra fissa che corrisponde ad ampiezzaintervallo
        print("da", LimiteInferiore, "a",LimiteSuperiore)





lista=[0.6406401169903435, 0.660248294842418, 0.00033887020724687744, 0.12881911899611587]



NumIntervalli=8
Conteggio=[0]*NumIntervalli
AmpiezzaIntervallo=1.0/NumIntervalli
for i in range(NumIntervalli):
    LimiteInferiore=i*AmpiezzaIntervallo
    LimiteSuperiore=LimiteInferiore+AmpiezzaIntervallo
    Conteggio[i]=NellIntervallo(lista, LimiteInferiore, LimiteSuperiore)
    print(Conteggio)

