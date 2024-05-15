def obtener_pares(lista):
   
    pares = [numero for numero in lista if numero % 2 == 0]
    return pares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = obtener_pares(lista_original)
print(f"Números pares en la lista: {lista_pares}")
