#11. Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.
n = int(input("Ingrese cuántas temperaturas va a introducir: "))  
sumaTemperaturas = 0  
temperaturaMaxima = float('-inf')  
temperaturaMinima = float('inf')  

for i in range(n):
    temperatura = float(input("Ingrese una temperatura: "))  

    sumaTemperaturas += temperatura   

    if temperatura > temperaturaMaxima:  
        temperaturaMaxima = temperatura

    if temperatura < temperaturaMinima:  
        temperaturaMinima = temperatura

temperaturaPromedio = sumaTemperaturas / n  

print(f"La temperatura más alta es: {temperaturaMaxima}")
print(f"La temperatura más baja es: {temperaturaMinima}")
print(f"La temperatura promedio es: {temperaturaPromedio}")
