def buscar_sable(lista):
    if lista == []:
        return -1
    if lista[0] == 'sable':
        return 0
    return 1 + buscar_sable(lista[1:])
