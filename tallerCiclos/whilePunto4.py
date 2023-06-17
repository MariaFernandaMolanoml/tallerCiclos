#4. Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 < num2:
    i = num1
    while i <= num2:
        print(i)
        i += 1
elif num2 < num1:
    i = num2
    while i <= num1:
        print(i)
        i += 1
else:
    print("Sus números son iguales o no son caracteres válidos")
