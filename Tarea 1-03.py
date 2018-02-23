# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:26:51 2018

@author: Felipe Coral
"""



    
    
       

while(1):
    NumIngresado, PartDec = 0.0,0.0
    # edicion sin sentido
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
        PartEnt=int(NumIngresado)
        Prueba = str(NumIngresado).split(".")
        PartDec=float("0."+Prueba[1])
        print(PartDec, "    ")
        
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
        
        print(EnteBin)
        print(DecBin)
        print("    ")
        
#        for i in range(0,23):
#            print(EnteBin[i])
#        print("     ")  
#        for i in range(0,23):
#            print(DecBin[i])
#        print("     ")
        while (EnteBin[cont] != 1):
            cont=cont+1
        
    
        while (DecBin[cont2] == 0):
            cont2=cont2+1
            
#        print(cont, cont2)
        
        
        cont=24-cont
        coma=cont-2
        cont2=24-cont2
        
        
        Union=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        k=0
        
#        print(cont, cont2)
        for k in range(0,cont2):
            Union[22-k]=DecBin[22-k]
#        print(k)
        for j in range(0,cont):
            Union[22-k]=EnteBin[22-j]
            k=k+1
#            
#        for i in range(0,23):
#            print(Union[i])
#        print("     ")
            
#        print(Union)
        cont=0
        while (Union[cont] != 1):
            cont=cont+1
        cont=cont+1
        r=0
        while (cont<=22):
            UnionD[r]=Union[cont]
            cont=cont+1
            r=r+1
#        for i in range(0,23):
#            print(UnionD[i])
#        print("     ")
#        print(UnionD)
        
        expo=coma+127
        EXPO=[0,0,0,0,0,0,0,0]
        for i in range(0,8):
            EXPO[7-i]=expo%2
            expo=expo/2
            expo=int(expo)
#        for i in range(0,8):
#            print(EXPO[i])
#        print("     ")
#        print(EXPO)
        
        Signo=0
        print("BINARIO EN IEEE754: ")
        print("SIGNO:",Signo)
        print("EXPONENTE:",EXPO)
        print("MANTISA:",UnionD)
#        for i in range(0,8):
#            print(EXPO[i])
#        for i in range(0,23):
#            print(UnionD[i])
    else:
        PartEnt=(-1*NumIngresado)
        PartEnt=int(NumIngresado)
        Prueba = str(NumIngresado).split(".")
        PartDec=float("0."+Prueba[1])
        print(PartDec, "    ")
        
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
        
        print(EnteBin)
        print(DecBin)
        print("    ")
        
#        for i in range(0,23):
#            print(EnteBin[i])
#        print("     ")  
#        for i in range(0,23):
#            print(DecBin[i])
#        print("     ")
        while (EnteBin[cont] != 1):
            cont=cont+1
        
    
        while (DecBin[cont2] == 0):
            cont2=cont2+1
            
#        print(cont, cont2)
        
        
        cont=24-cont
        coma=cont-2
        cont2=24-cont2
        
        
        Union=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        k=0
        
#        print(cont, cont2)
        for k in range(0,cont2):
            Union[22-k]=DecBin[22-k]
#        print(k)
        for j in range(0,cont):
            Union[22-k]=EnteBin[22-j]
            k=k+1
#            
#        for i in range(0,23):
#            print(Union[i])
#        print("     ")
            
#        print(Union)
        cont=0
        while (Union[cont] != 1):
            cont=cont+1
        cont=cont+1
        r=0
        while (cont<=22):
            UnionD[r]=Union[cont]
            cont=cont+1
            r=r+1
#        for i in range(0,23):
#            print(UnionD[i])
#        print("     ")
#        print(UnionD)
        
        expo=coma+127
        EXPO=[0,0,0,0,0,0,0,0]
        for i in range(0,8):
            EXPO[7-i]=expo%2
            expo=expo/2
            expo=int(expo)
#        for i in range(0,8):
#            print(EXPO[i])
#        print("     ")
#        print(EXPO)
        
        Signo=1
        print("BINARIO EN IEEE754: ")
        print("SIGNO:",Signo)
        print("EXPONENTE:",EXPO)
        print("MANTISA:",UnionD)
#        for i in range(0,8):
#            print(EXPO[i])
#        for i in range(0,23):
#            print(UnionD[i])
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        