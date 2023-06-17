#4. Sumar pares desde 0 hasta el número que indique el usuario
n = int(input("Ingrese un número: ")) 
total = 0  

for i in range(0, n+1, 2):  
    total += i
print(f"La suma de tus numeros pares es {total}")


