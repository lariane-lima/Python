def fatoracao(n):
    print(n,'=', end = ' ')
    i = 2
    while(n > 1):
        div = n % i
        if (div == 0):
            n = n / i
            print(i,'*', end = ' ')
        else:
            i += 1
    print(1)

n = int(input('Digite um número natural não nulo: '))
fatoracao(n)
