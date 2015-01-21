def DaA(Iv, Lungh): #Come Dividere in intervalli qualunque altro numero
        CifraFissa=Iv/Lungh #Iv è uguale al numero da dividere in n intervalli
        for i in range(Lungh):#Per tutti i numeri nel raggio di Lungh fai ciò:
            limiteinferiore=CifraFissa*i#limiteinferiore sarà il prodotto tra una cifra fissa per tutti e i
            limitesuperiore=limiteinferiore+CifraFissa#limitesuperiore somma tra limiteinferiore e una cifra fissa
            print("da",limiteinferiore, "a", limitesuperiore)




        
