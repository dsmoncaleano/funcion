def es_primo(numero):
    
    if numero <= 1:
        return False
    
    
    if numero == 2:
        return True
    
    
    if numero % 2 == 0:
        return False
    
    
    raiz_cuadrada = int(numero**0.5) + 1
    for divisor in range(3, raiz_cuadrada, 2):
        if numero % divisor == 0:
            return False
    
    return True

numeros_a_verificar = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
resultados = {numero: es_primo(numero) for numero in numeros_a_verificar}

for numero, es_primo_val in resultados.items():
    print(f"¿El número {numero} es primo? {'Sí' if es_primo_val else 'No'}")
