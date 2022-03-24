def éPrimo(k):
    divisor = 2
    divisao = k % divisor
    x = 0
    while (divisor < k):
        divisao = k % divisor
        divisor = divisor + 1
        if (divisao == 0):
            x += 1
    return (x)


def maior_primo(k):
    x = éPrimo(k)
    if (x > 0):
        while(x > 0):
            x -= x
            k -= 1
            x = éPrimo(k)
        return (k)
    else:
        return (k)
    return print(k)
        

   

