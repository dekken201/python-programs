entrada = #'ZEQSW ETVIRHIV GVMTXSKVEJME'#"DKFAJWKPAILNKRW" 
saida = []
contador = 0
print("STRING ORIGINAL: "+entrada)
while True:
	for i in range(0,len(entrada)):
		if ord(entrada[i]) == 32:
			saida.append(chr(32))
		elif ord(entrada[i])+(contador) <= 90:
			saida.append(chr(ord(entrada[i])+(contador)))
		else:
			saida.append(chr((ord(entrada[i])+(contador))-26))
	print(str(contador)+" "+str(saida))
	if (contador == 25):
		break
	else:
		contador += 1
		saida = []

