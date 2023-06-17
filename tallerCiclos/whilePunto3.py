#3. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
n = int(input("Ingrese un número: "))
total = 0
impares = 0
i = 1

while i <= n:
    total += i
    impares += 1
    i += 2

print(f"La suma de tus números impares es {total}")
print(f"La cantidad de impares sumados es: {impares}")
