#5. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
n = int(input("Ingrese un número: ")) 
total = 0 
impares = 0

for i in range(1, n+1, 2):  
    total += i
    impares += 1
print(f"La suma de tus numeros impares es {total}")
print(f"La cantidad de impares sumados son: {impares}")


