def Sequenza(n):
    while(n!=1):
        print(n)
    if(n%2==0):
        n=n/2
        print(n)
    else:
        n=n*3+1
        print(n)
Sequenza(3)
