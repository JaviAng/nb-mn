import math
import numpy as np
import scipy
import bitstring

numero = float (input('\nIntroduce un numero:'))
valor_absoluto = math.fabs(numero)
parte_entera = int(valor_absoluto)
parte_decimal = valor_absoluto - parte_entera

print('\neste es el numero entero:',parte_entera)
print('\neste es el numero decimal:',parte_decimal)

def Binarizar_Entero(Entero):
        Binario = ''
        while Entero // 2 !=0:
            Binario = str(Entero % 2)+Binario
            Entero = Entero // 2
        return str(Entero) + Binario
            
binario_1 = Binarizar_Entero(parte_entera)    
print('\nnumero entero binarizado:',binario_1)

if parte_decimal > 0.0:
    def Binarizar_Decimal(parte_decimal):
        Binario=''
        while parte_decimal != 0 :
            parte_decimal = parte_decimal * 2
            parte_decimal_entera = int (parte_decimal)
            parte_decimal = parte_decimal - parte_decimal_entera
            Binario = Binario + str(parte_decimal_entera)
        return str(parte_decimal_entera) + Binario

    binario_2 = Binarizar_Decimal(parte_decimal)    
    print('\nnumero decimal binarizado:',binario_2)
else:
    binario_2= '0'
       
def Binarizar_coma(Entero):
        Binario = ''
        while Entero // 2 !=0:
            Binario = str(Entero % 2)+Binario
            Entero = Entero // 2
        return str(Entero) + Binario

coma = (len(binario_1) -1 ) +127
print('\ncorrimiento +numero estandar:',coma)
    
binario_coma = Binarizar_coma(coma)    
print('\nbinarizado de lo anterior:',binario_coma)
    
if numero > 0:
    print('0',binario_coma,binario_1+binario_2.ljust(32,'0'),'\n')
else:
    print('1',binario_coma,binario_1+binario_2.ljust(32,'0'),'\n')





    


