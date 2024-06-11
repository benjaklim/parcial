def listar_inversa(lista):
    if not lista:
        return
    print(lista[-1])
    listar_inversa(lista[:-1])
    
mi_lista = [1, 2, 3, 4, 5, 6, 7]
listar_inversa(mi_lista)
