def factorial(*n):
    for x in n:
        fact = 1
        for y in range(1, x + 1):
            fact *= y  # Como indica @César en los comentarios, puedes sustituir esta línea así
        print(fact)

factorial(7)