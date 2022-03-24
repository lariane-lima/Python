valor = int(input('Digite um número inteiro: '))

#-----------------------------
# últimoDígito = valor % 10
# novoValor = valor // 10 
#-----------------------------

anterior = 10
TemIgual = False
while (valor != 0 and not TemIgual):
	digito = valor % 10
	if (digito == anterior):
		print('sim')
		TemIgual = True
	valor = valor //10
	anterior = digito

if (not TemIgual):
	print('não')
