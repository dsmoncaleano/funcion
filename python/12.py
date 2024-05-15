def es_palindromo(cadena):
   
    cadena_limpia = ""
    for caracter in cadena:
        if 'A' <= caracter <= 'Z':  
            cadena_limpia += chr(ord(caracter) + 32)
        elif 'a' <= caracter <= 'z' or '0' <= caracter <= '9':  
            cadena_limpia += caracter
    
    return cadena_limpia == cadena_limpia[::-1]

frases = [
    "Ana",
    "Anita lava la tina",
    "A man, a plan, a canal, Panama",
    "No es palíndromo",
    "La ruta natural",
]

for frase in frases:
    resultado = es_palindromo(frase)
    print(f"¿'{frase}' es un palíndromo? {'Sí' if resultado else 'No'}")

