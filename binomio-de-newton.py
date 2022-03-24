n = int(input('Digite o coeficiente n: '))
k = int(input('Digite o coeficiente k: '))

def fatorial (p):
    multiplicação = 1
    if (p != 0):
        while (p != 0):
            multiplicação = multiplicação * p
            p = p - 1
        return (multiplicação)
    else:
        return (int('1'))

num_binomial = (fatorial (n))/((fatorial (k))*(fatorial (n-k)))
print('O resultado é: ', num_binomial)
