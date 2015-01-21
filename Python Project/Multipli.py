
def StampaMultipli(n, Grandezza):
    i=1    
    while(i<=Grandezza):
        print(n*i, '\t', )
        i=i+1
    print()

def TabellaMoltiplicazioneGenerica(Grandezza):
    i=1
    while(i<=Grandezza):
        StampaMultipli(i, Grandezza)
        i=i+1
        
TabellaMoltiplicazioneGenerica(7)

       
        
        
