print("              TAREA 1        ")
print("CONVERCION DECIMAL A BINARIO")
print("FELIPE CORAL OTALORA 161003611")
print("BRAYAN J. SALDARRIAGA 161003640")

while(1):
    NumIngresado, PartDec = 0.0,0.0
    
    EnteBin=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    DecBin=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    PartEnt=0
    aux=0
    coma=0
    expo=0
    Signo=0
    cont=0
    cont2=0
    
    UnionD=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    NumIngresado = float(input("INGRESE EL NUMERO: "))
    if NumIngresado>=0:
        if NumIngresado==0: 
            print("                   BINARIO EN IEEE754     ")
            print("SIGNO: 0")
            print("EXPONENTE: [0,0,0,0,0,0,0]")
            print("MANTISA:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
        else:
            PartEnt=int(NumIngresado)
            Prueba = str(NumIngresado).split(".")
            PartDec=float("0."+Prueba[1])
            a=str(PartDec)
            b=len(a)
            if(b>6):
                a=a[0:6]
                PartDec=float(a)

            for i in range(0,23):
                EnteBin[22-i]=(PartEnt%2)
                PartEnt=PartEnt/2
                PartEnt=int(PartEnt)
            
            for i in range(0,23):
                PartDec=PartDec*2
                aux = int(PartDec)
                Prueba = str(PartDec).split(".")
                PartDec=float("0."+Prueba[1])
                DecBin[22-i]=aux

            while (EnteBin[cont] != 1):
                cont=cont+1
            
        
            while (DecBin[cont2] == 0 and cont2<22):
                cont2=cont2+1  
            
            cont=24-cont
            coma=cont-2
            cont2=24-cont2
            
            
            Union=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            k=0

            for k in range(0,cont2):
                Union[22-k]=DecBin[22-k]
            for j in range(0,cont):
                Union[22-k]=EnteBin[22-j]
                k=k+1
            cont=0

            while (Union[cont] != 1):
                cont=cont+1
            cont=cont+1

            r=0

            while (cont<=22):
                UnionD[r]=Union[cont]
                cont=cont+1
                r=r+1

            expo=coma+127
            EXPO=[0,0,0,0,0,0,0,0]

            for i in range(0,8):
                EXPO[7-i]=expo%2
                expo=expo/2
                expo=int(expo)
            
            Signo=0
            print("BINARIO EN IEEE754: ")
            print("SIGNO:",Signo)
            print("EXPONENTE:",EXPO)
            print("MANTISA:",UnionD)
    else:
        PartEnt=(-1*NumIngresado)
        PartEnt=int(NumIngresado)
        Prueba = str(NumIngresado).split(".")
        PartDec=float("0."+Prueba[1])
        
        for i in range(0,23):
            EnteBin[22-i]=(PartEnt%2)
            PartEnt=PartEnt/2
            PartEnt=int(PartEnt)
        
        for i in range(0,23):
            PartDec=PartDec*2
            aux = int(PartDec)
            Prueba = str(PartDec).split(".")
            PartDec=float("0."+Prueba[1])
            DecBin[22-i]=aux

        while (EnteBin[cont] != 1):
            cont=cont+1
        
    
        while (DecBin[cont2] == 0 and cont2<22):
            cont2=cont2+1
  
        cont=24-cont
        coma=cont-2
        cont2=24-cont2
        
        
        Union=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        k=0
        
        for k in range(0,cont2):
            Union[22-k]=DecBin[22-k]
        for j in range(0,cont):
            Union[22-k]=EnteBin[22-j]
            k=k+1
        cont=0
        while (Union[cont] != 1):
            cont=cont+1
        cont=cont+1
        r=0
        while (cont<=22):
            UnionD[r]=Union[cont]
            cont=cont+1
            r=r+1
        expo=coma+127
        EXPO=[0,0,0,0,0,0,0,0]
        for i in range(0,8):
            EXPO[7-i]=expo%2
            expo=expo/2
            expo=int(expo)
       
        Signo=1
        print("            BINARIO EN IEEE754         ")
        print("SIGNO:",Signo)
        print("EXPONENTE:",EXPO)
        print("MANTISA:",UnionD)

