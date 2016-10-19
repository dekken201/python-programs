#Versão refatorada, sem comentários, utilizando funções.

#CRIAÇÃO DE VARIÁVEIS GLOBAIS:
choice = 0
res = 0
resto = []
x = 0
i = 0

#FUNÇÕES:
def dec_to_hexa():
		for i in range(0,len(resto),1):
			if resto[i] !=(resto[i] >= 0 or resto[i] <=9):
				if (resto[i] == 10):
					resto[i] = 'A'
				elif (resto[i] == 11):
					resto[i] = 'B'
				elif (resto[i] == 12):
					resto[i] = 'C'
				elif (resto[i] == 13):
					resto[i] = 'D'
				elif (resto[i] == 14):
					resto[i] = 'E'
				elif (resto[i] == 15):
					resto[i] = 'F'
			else:
				pass

def hexa_to_dec():
	for i in range(0,len(number),1):
		x = 0
		x = ord(number[i])
		if ((x >= 65) and (x <= 70)) or ((x >= 97) and (x <= 102)):
			if (x == 65) or (x == 97):
				number[i] = 10
			elif (x == 66) or (x == 98):
				number[i] = 11
			elif (x == 67) or (x == 99):
				number[i] = 12
			elif (x == 68) or (x == 100):
				number[i] = 13
			elif (x == 69) or (x == 101):
				number[i] = 14
			elif (x == 70) or (x == 102):
				number[i] = 15
		else:
			number[i] = int(number[i])	

#INÍCIO DO CÓDIGO

print('''
--------------------------------------------------------------
|	CONVERSOR DE BASES                                   |
| Binário -> Decimal = '1', Decimal -> Binário = '2'         |
| Hexadecimal -> Decimal = '3', Decimal -> Hexadecimal = '4' |
| Hexadecimal -> Binário = '5', Binário -> Hexadecimal = '6' |
--------------------------------------------------------------
	 ''')
valid = False
while valid != True:
	choice = int(input("Digite o número equivalente a operação desejada --->"))
	if (choice >= 1 and choice <= 6):
		valid = True
	else:
		print("Escolha inválida!")
		valid = False

if choice == 1:
	print("-- Binário -> Decimal --\n")
	number = (list(reversed(input("Digite o número a ser convertido para decimal: "))))
	number = [int(i) for i in number]	
	for i in range(0,len(number),1):
		number[i] = (number[i] * (2 ** i))
		res = number[i] + res
	print ("O seu número em decimaĺ é: ",res)

elif choice == 2:
	print("-- Decimal -> Binário --\n")
	number = int(input("Digite o número a ser convertido para binário: "))
	while (number != 0):
		resto.append(number % 2)
		number = number // 2
	resto.reverse()
	print ("O seu número, em binário, é: ",resto)
		
elif choice == 3:
	print("-- Hexadecimal -> Decimal --\n")
	number = (list(reversed(input("Digite o número a ser convertido para decimal: "))))
	hexa_to_dec()
	for i in range(0,len(number),1):
		number[i] = (number[i] * (16 ** i))
		res = number[i] + res
	print (number)
	print ("O seu número em hexadecimaĺ é: ",res)

elif choice == 4:
	print("-- Decimal -> Hexadecimal --\n")
	number = int(input("Digite o número a ser convertido para hexadecimal: "))
	while (number != 0):
		resto.append(number % 16)
		number = number // 16
	resto.reverse()
	dec_to_hexa()
	print ("O seu número, em hexadecimal, é: ",resto)

elif choice == 5:
	print("-- Hexadecimal -> Binário --\n")
	number = (list(reversed(input("Digite o número a ser convertido para binário: "))))
	hexa_to_dec()
	res = []
	for i in range(0, len(number), 1):
		while number[i] != 0:
			resto.append(number[i] % 2)
			number[i] = (number[i] // 2)
		if len(resto) < 4:
			for x in range(len(resto), 4, 1):
				resto.append(0)
		resto.reverse()
		number[i] = resto
		resto = []
	number.reverse()
	print(number)

elif choice == 6:
	print("-- Binário -> Hexadecimal --\n")
	number = (list(reversed(input("Digite o número a ser convertido para hexadecimal: "))))
	number = [int(i) for i in number]
	while (i < len(number)):
		if (x == 3) or (i==len(number)-1):
			number[i] = (number[i] * (2 ** x))
			res = number[i] + res
			resto.append(res)
			res = 0
			i = i + 1
			x = 0
		else:
			number[i] = (number[i] * (2 ** x))
			res = number[i] + res
			i = i + 1
			x = x + 1
	resto.reverse()
	dec_to_hexa()
	print ("O seu número, em hexadecimal, é: ",resto)