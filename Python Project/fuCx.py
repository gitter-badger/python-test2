def factx(x):
    while(x<2048):
        import math
        print("la radice quadrata di ", x),print("è", math.sqrt(x)), print('\t')
        print("il logaritmo di", x), print("è", math.log(x)), print('\t')
        x=x*2.0

primo=input("digita un numero:")
primo=float(primo)
operazione=factx(primo)
