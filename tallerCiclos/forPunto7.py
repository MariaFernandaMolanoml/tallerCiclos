#5. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
tabla = int(input("Ingrese la tabla de multiplicar que desea (1 al 10): "))

for i in range(1, 11):
    resultado = tabla * i
    print(tabla, "x", i, "=", resultado)