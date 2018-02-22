import os
def decimal_binario (decimal):

	if decimal < 0 : 	              
		signo = '1'
	else : 
		signo = '0'

	decimal = abs(decimal)   			
	a = int (decimal)
	b= decimal - a
	binario = ''
	while a > 1 :
		binario = str(a % 2) + binario  
		a = a // 2		
	vector = str (a) + binario
	coma = (len(vector) - 1) + 127
	binario_1 = ''
	while coma > 1 :
		binario_1 = str(coma % 2) + binario_1  
		coma = coma // 2


	binario_2 = ''
	while b != 0 :                       
		b = b * 2
		parte_entera = int (b)
		b = b - parte_entera 
		binario_2 = binario_2 + str(parte_entera)
	vector = vector + str (binario_2)
	muestro = ((str (signo) + str (coma) + binario_1 + vector[1:]).ljust(32,'0')) 	
	muestro_1 = ''
	for i in range (32):
		muestro_1 = muestro_1 + str (muestro[i]) 

	return muestro_1

valida = '' 		
while valida != 'no':
	os.system('cls')
	numero = float (input ('ingrese numero: '))
	print (decimal_binario (numero))
	valida = input ('desea continuar si o no: ')
