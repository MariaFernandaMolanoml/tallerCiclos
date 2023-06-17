#1. Suma de los n primeros números, solicite al usuario el numero de elementos a sumar
n=int(input("Digite su numero: "))
total= 0

for numeros in range(1, n + 1):
    total += numeros
print(f"La suma de los {n} primeros numeros es {total} ")
