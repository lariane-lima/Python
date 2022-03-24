def entra_dados(): # solicita dados e já chama a validação
  y = True
  z = True
  while(type(y) != list and type(z) != list):
    x = input('Insira a sequência com seus dígitos binários. Atenção, insira apenas os bits sem nenhum espaçamento, e só é válido 0 e 1. ')
    m = input('Insira a sequência com a máscara de binários. Atenção, insira apenas os bits sem nenhum espaçamento, e só é válido 0 e 1. ')
    x = list(x)
    m = list(m)
    y, z = valida_numeros(x, m)
  return x, m

def valida_numeros(x, m): # validação dos dados de entrada
  controle = [x, m]
  for j in range(2):
    try:
      for i in range(len(controle[j])): # verificação se é numero
        w = (int(controle[j][int(i)]))
        if (w > 1 or w < 0):
          print('Algo deu errado, as séries devem conter somente binários!')
          return False, False
      if (len(controle[j]) != 16): # verificação se contem 16bits
        print('Algo deu errado, as séries devem conter exatamente 16 bits!')
        return False, False
    except ValueError: # caso seja inserida algo que não seja integer
      print('Algo deu errado, certifique-se de inserir somente números!')
      return False, False
  digitos = controle[0]
  mascara = controle[1]
  return digitos, mascara

print('Para que a sequência seja comprimida, precisarei de duas sequências de 16 bits, uma com para seus dados e outra para a máscara a ser usada!')
digitos, mascara = (entra_dados())

digito_inverso = digitos[::-1]
mascara_inversa = mascara[::-1]
r = []
for i in range(16):
  if (mascara_inversa[i] == '1'):
    r.append(digito_inverso[i]) # cria lista r
while (len(r) < 16):
  r.append('0')
r = r[::-1]

lista = [[], [], [], []]
start = 0
end = 4
r_separado = []
for k in range(len(lista)): # divide os blocos de 16 bits em 4
    r_separado.append(r[start:end])
    x = 0
    start += 4
    end += 4
while(x < 4): # concatena e tira da lista para que retorne de maneira mais inteligível
    teste = ''.join(r_separado[x])
    x += 1
    print(teste, end=' ')