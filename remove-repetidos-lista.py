def remove_repetidos(lista):
    i = 0
    for item in lista:
        while(i < len(lista)):
            for item in lista:
                if(lista[i] == item):
                    del lista[i]
                    i += 1
    return lista
