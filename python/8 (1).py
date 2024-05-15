def contar_mayusculas_minusculas(cadena):
  
    conteo = {'mayusculas': 0, 'minusculas': 0}
    
    for caracter in cadena:
        if caracter.isupper():
            conteo['mayusculas'] += 1
        elif caracter.islower():
            conteo['minusculas'] += 1
    
    return conteo


cadena = "Hola Mundo! Esto Es Una Prueba."
resultado = contar_mayusculas_minusculas(cadena)
print(f"Letras mayúsculas: {resultado['mayusculas']}")
print(f"Letras minúsculas: {resultado['minusculas']}")

