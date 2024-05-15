def contar_mayusculas_minusculas(cadena):
    """
    Calcula el número de letras mayúsculas y minúsculas en una cadena.
    
    Parámetros:
    cadena (str): La cadena a analizar.
    
    Retorna:
    dict: Un diccionario con el conteo de letras mayúsculas y minúsculas.
    """
    conteo = {'mayusculas': 0, 'minusculas': 0}
    
    for caracter in cadena:
        if caracter.isupper():
            conteo['mayusculas'] += 1
        elif caracter.islower():
            conteo['minusculas'] += 1
    
    return conteo

# Ejemplo de uso:
cadena = "Hola Mundo! Esto Es Una Prueba."
resultado = contar_mayusculas_minusculas(cadena)
print(f"Letras mayúsculas: {resultado['mayusculas']}")
print(f"Letras minúsculas: {resultado['minusculas']}")
