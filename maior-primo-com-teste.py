def éPrimo(k):
    divisor = 2
    divisao = k % divisor
    x = 0
    while (divisor < k):
        divisao = k % divisor
        divisor = divisor + 1
    if (divisao == 0):
        x = x + 1
    return (x)


def maior_primo(k):
    x = éPrimo(k)
    if (x > 0):
        while(x > 0):
            x = x - x
            k = k - 1
            x = éPrimo(k)
        return (k)
    else:
        return (k)
    return print(k)


def test_maior_primo7():
    assert maior_primo(7) == 7

def test_maior_primo6():
    assert maior_primo(6) == 5

def test_maior_primo5():
    assert maior_primo(5) == 5

def test_maior_primo100():
    assert maior_primo(100) == 97
    
