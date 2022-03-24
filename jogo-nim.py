# n é numero de peças
# m é numero maximo que pode pegar de peças (1 é o minimo)
# j é oq o jogador tirou de peças
# b é oq boot tirou de peças
#------------------------------------------------------------------
def computador_escolhe_jogada(n, m):
    if (n <= m):
        b = n
    else:
        y = 0
        x = 0
        divisao = 1
        while (divisao != 0):
            b = x + 1
            y = n - b
            divisao = y % (m+1)
            if b > m:
                b = m
                divisao = 0
            if (divisao != 0):
                x = x + 1
    print('O computador tirou', b, 'peça(s).')
    return b
#------------------------------------------------------------------
#pede valor da jogada do usuario, e analisa, se for valido ok, se não for, pede pra colocar um valido
def usuario_escolhe_jogada(n, m):
    valor = int(input('Quantas peças você vai tirar? '))
    while (not((valor >= 1) and (valor <= m))):
        print('Oops! Jogada inválida! Tente de novo.')
        valor = int(input('Quantas peças você vai tirar? '))
    j = valor
    print('Você tirou', j, 'peça(s).')
    return (j)
#------------------------------------------------------------------
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    while(n <= m):
        print('Oops! Opção inválida! Tente de novo.')
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
    #Usuário começa!
    if ((n % (m+1)) == 0):
        if (n > 0):
            print('Você começa!')
            while (n > 0):
                j = usuario_escolhe_jogada(n, m)
                n = n - j
                print('Agora resta apenas', n, 'peça(s) no tabuleiro.')
                if(n > 0):
                    b = computador_escolhe_jogada(n, m)
                    n = n - b
                    print('Agora resta apenas', n, 'peças no tabuleiro.')
            if(n == 0):
                return print('Fim do jogo! O computador ganhou!')
    #Computador começa!
    else:
        print('Computador começa!')
        while (n > 0):
            b = computador_escolhe_jogada(n, m)
            n = n - b
            print('Agora resta apenas', n, 'peças no tabuleiro.')
            if(n > 0):
                j = usuario_escolhe_jogada(n, m)
                n = n - j
                print('Agora resta apenas', n, 'peça(s) no tabuleiro.')
        if(n == 0):
            return print('Fim do jogo! O computador ganhou!')
#------------------------------------------------------------------
c = int(input('Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
while((c != 1) and (c!= 2)):
    print('Oops! Opção inválida! Tente de novo.')
    c = int(input('Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
num_rodada = 1
if (c == 2):
    print('Voce escolheu um campeonato!')
    print('**** Rodada', num_rodada,'****')
    num_rodada = num_rodada + 1
    partida()
    print('**** Rodada', num_rodada,'****')
    num_rodada = num_rodada + 1
    partida()
    print('**** Rodada', num_rodada,'****')
    partida()
    print('**** Final do campeonato! ****')
    print('Placar: Você 0 X 3 Computador')
else:
    print('Voce escolheu uma partida!')
    partida()
