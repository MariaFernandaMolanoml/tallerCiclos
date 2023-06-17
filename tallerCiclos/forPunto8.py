#5. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
n = int(input("Ingrese la cantidad de notas: ")) 
suma = 0   

for i in range(1,n+1):
    nota = float(input("Ingrese una nota: "))  
    suma += nota  

promedio = suma / n 

print("El promedio es:", promedio)
