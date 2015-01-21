def Scambia(x, y):
    return y, x


def GLC(n):
    s=[0]*n
    for i in range(n):
        import random
        s[i]=random.random()
        print(s)

def UL(Lista1, Lista2):
    print(Lista1 + Lista2)

a=[0.4917316996540183, 0.17175046784738257, 0.224902396774881, 0.719103036552633]
b=[0.6634948834408754, 0.654406063897225, 0.5010100536414486, 0.7845341191114874]

def Analizza(stringa, parola, posizione):
    conteggio=0
    for i in stringa[posizione:]:
        if(i==parola):
            conteggio=conteggio+1
            print(conteggio)
        else:
            pass

