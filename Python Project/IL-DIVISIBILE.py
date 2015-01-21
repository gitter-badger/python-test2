
def Divisibile(n, grandezza):
    i=1
    while(i<=grandezza):
        if(n%i==0):
            print(n, "è divisibile per", i)
        i=i+1

primo=input("digita il numero di cui vuoi sapere i sui divisori: ")
secondo=input("Reinserisci il numero: ")
primo=int(primo)
secondo=int(secondo)
op=Divisibile(primo, secondo)
