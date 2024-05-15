def obtener_unicos(lista):
    
    unicos = list(set(lista))
    return unicos
    
lista_original = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
lista_unicos = obtener_unicos(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista con elementos únicos: {lista_unicos}")
