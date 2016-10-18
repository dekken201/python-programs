'''Fazer:
Refatorar código com uso de funções;
Tentar usar try/except na parte de hexadecimal
Verificar reversed lists na apresentação dos resultados
Melhorar fórmula da escolha 5, tá uma porcaria
'''

#Recebe a escolha do usuário para qual operação realizar
choice = 0
valid = False
while valid != True:
	choice = int(input("Binário -> Decimal = '1', Decimal -> Binário = '2'\nHexadecimal -> Decimal = '3', Decimal -> Hexadecimal = '4'\nHexadecimal -> Binário = '5', Binário -> Hexadecimal = '6'\n---->"))
	if (choice >= 1 and choice <= 6):
		valid = True
	else:
		print("Escolha inválida!")
		valid = False


#Cria a variável do resultado e do resto:
res = 0
resto = []
if choice == 1:
	print("-- Binário -> Decimal --\n")
	#Recebe o número, em binário, inverte a ordem para facilitar nas próximas operações,
	#separa cada número em um caracter e armazena em uma lista.
	number = (list(reversed(input("Digite o número a ser convertido para decimal: "))))
	#Converte os elementos da lista, atualmente Str, em int:
	number = [int(i) for i in number]	
	#Realiza um for loop com a operação principal da conversão binário -> decimal:
	for i in range(0,len(number),1):
		number[i] = (number[i] * (2 ** i))
		res = number[i] + res
	#A linha abaixo é para teste, para verificar se o número foi lido e inserido corretamente na lista. Para ver esse teste, basta apagar o #.
	#print (number)
	print ("O seu número em decimaĺ é: ",res)

elif choice == 2:
	print("-- Decimal -> Binário --\n")
	#Cria a variável do resto:
	#Recebe o número em decimal:
	number = int(input("Digite o número a ser convertido para binário: "))
	#Operação principal:
	while (number != 0):
		resto.append(number % 2)
		number = number // 2
	#Inverte a lista, pois a operação foi realizada da esquerda pra direita, quando o correto é da direita pra esquerda.
	resto.reverse()
	print ("O seu número, em binário, é: ",resto)
	#A linha abaixo é para teste, para verificar se o número foi dividido corretamente sem resto. Para ver esse teste, basta apagar o #.
	#print(number)
	
elif choice == 3:
	print("-- Hexadecimal -> Decimal --\n")
	number = (list(reversed(input("Digite o número a ser convertido para decimal: "))))
	#Este loop serve pra verificar se é um número ou uma letra, se for uma letra, converte para seu valor específico.
	#Se for número, converte para int.
	for i in range(0,len(number),1):
		#Cria a variável x, que vai segurar o valor do caractere em ASCII, para facilitar a conversão das letras
		#Exemplo 'a' = 97 em ASCII.
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
	
	for i in range(0,len(number),1):
		number[i] = (number[i] * (16 ** i))
		res = number[i] + res
	print (number)
	print ("O seu número em hexadecimaĺ é: ",res)

elif choice == 4:
	print("-- Decimal -> Hexadecimal --\n")
	number = int(input("Digite o número a ser convertido para hexadecimal: "))
	#Mesmo padrão de conversão já usado anteriormente, porem dividindo por 16
	while (number != 0):
		resto.append(number % 16)
		number = number // 16
	resto.reverse()
	#Após ter os valores crus, converte os valores acima de 9 em suas respectivas letras em hexadecimal.
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
	print ("O seu número, em hexadecimal, é: ",resto)

elif choice == 5:
	print("-- Hexadecimal -> Binário --\n")
	number = (list(reversed(input("Digite o número a ser convertido para binário: "))))
	for i in range(0,len(number),1):
		#Cria a variável x, que vai segurar o valor do caractere em ASCII, para facilitar a conversão das letras
		#Exemplo 'a' = 97 em ASCII.
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
	#Faz o calculo para converter para binário:
	res = []
	#Basicamente, ele roda a lista dos números já convertidos para decimal, e transforma cada
	#número em uma sublista com os 4 dígitos em binários que o representa.
	for i in range(0, len(number), 1):
		while number[i] != 0:
			resto.append(number[i] % 2)
			number[i] = (number[i] // 2)
			#Se o número em binário não tiver 4 bits, adiciona zeros a esquerda pra compensar.
		if len(resto) < 4:
			for x in range(len(resto), 4, 1):
				resto.append(0)
		#Inverte os dígitos convertidos para deixá-los na ordem correta
		resto.reverse()
		number[i] = resto
		resto = []
	number.reverse()
	print(number)

elif choice == 6:
	print("-- Binário -> Hexadecimal --\n")
	number = (list(reversed(input("Digite o número a ser convertido para hexadecimal: "))))
	number = [int(i) for i in number]
	#Cria duas variáveis, o i para indicar o índice na lista, e o x, pra fazer a contagem dos 4 dígitos por caractere em hexadecimal
	x = 0
	i = 0
	#Loop principal, com duas condicionais. Seguindo o mesmo pŕincípio do conversor binário - decimal, quando a variável res recebe
	#4 valores, fechando o dígito em hexadecimal, um novo item é criado até fechar a quantidade de caracteres em binário digitadas.
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
	#Inverte os resultados, para facilitar a leitura e deixar o padrão correto:
	resto.reverse()
	#Converte os caracteres > 9 para seu equivalente hexadecimal
	for i in range(0,len(resto),1):
		if resto[i] != (resto[i] >= 0 or resto[i] <=9):
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
	print ("O seu número, em hexadecimal, é: ",resto)




