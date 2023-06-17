#8. Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
numero = int(input("Ingrese un número entero mayor que cero: "))
divisor = 1

while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1

if numero <= 0:
    print("Ingrese un numero mayor a 0")
