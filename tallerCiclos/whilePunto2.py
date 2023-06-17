#2. Sumar pares desde 0 hasta el número que indique el usuario.

n = int(input("Ingrese un número: "))
total = 0
i = 0

while i <= n:
    total += i
    i += 2

print(f"La suma de tus números pares es {total}")



