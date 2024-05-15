menu = ("""
1. Rectangulo
2. Cuadrado
3. paralelogramo
4. Rombo
5. Trapecio
6. Trinagulo
7. Triangulo equilatero
8. Triangulo rectangulo
9. Poligono regular

Ingrese el número correspondiente a la figura que desea calcular el área: """)
opcion=int(input(menu))

if opcion == 1:
  a = float(input("Digite el valor de a "))
  b = float(input("Digite el valor de b"))
  area = a * b
  print(f"El area del rectangulo es {area}")
elif opcion == 2:
  a = float(input("Digite el valor de a "))
  area = a ** 2
  print(f"El area del cuadrado es {area}")
elif opcion == 3:
  b = float(input("Digite el valor de b "))
  h = float(input("Digite el valor de h"))
  area = b * h
  print(f"El area del paralelogramo es {area}")
elif opcion == 4:
  ac = float(input("Digite el valor de ac "))
  bd = float(input("Digite el valor de bd"))
  area = ac * bd / 2
  print(f"El area del rombo es {area}")
elif opcion == 5:
  a = float(input("Digite el valor de a "))
  b = float(input("Digite el valor de b"))
  h = float(input("Digite el valor de h"))
  area = (a + b) * h / 2
  print(f"El area del trapecio es {area}")
elif opcion == 6:
  a = float(input("Digite el valor de a "))
  h = float(input("Digite el valor de h"))
  area = a * h / 2
  print(f"El area del triangulo es {area}")
elif opcion == 7:
  a = float(input("Digite el valor de a "))
  area = a ** 2 * 3 ** 0.5 / 4
  print(f"El area del triangulo equilatero es {area}")
elif opcion == 8:
  a = float(input("Digite el valor de a "))
  c = float(input("Digite el valor de c"))
  area = a * c / 2
  print(f"El area del triangulo rectangulo es {area}")
elif opcion == 9:
  p = float(input("Digite el valor de p "))
  apotema = float(input("Digite el valor de la apotema"))
  area = p * apotema / 2
  print(f"El area del poligono regular es {area}")