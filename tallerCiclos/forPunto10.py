#10. Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
numero = int(input("Ingrese un número: "))  

print("Los divisores de", numero, "son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
