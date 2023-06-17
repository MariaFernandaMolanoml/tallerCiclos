#6. Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio
n = int(input("Ingrese la cantidad de notas a capturar: "))
sumaNotas = 0
contador = 0

while contador < n:
    nota = float(input("Ingrese la nota: "))
    sumaNotas += nota
    contador += 1

promedio = sumaNotas / n
print("El promedio de las notas es:", promedio)
