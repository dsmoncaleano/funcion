def esta_en_rango(inicio, numero, final):
    if inicio > final:
        raise ValueError("El valor de inicio debe ser menor o igual al valor final del rango")
    
    return inicio <= numero <= final
    
rango_inicio = 10
numero_a_comprobar = 15
rango_final = 20

if esta_en_rango(rango_inicio, numero_a_comprobar, rango_final):
    print(f"El número {numero_a_comprobar} está dentro del rango de {rango_inicio} a {rango_final}.")
else:
    print(f"El número {numero_a_comprobar} no está dentro del rango de {rango_inicio} a {rango_final}.")