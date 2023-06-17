#5. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
num1= int(input("Dijite un numero: "))
num2= int(input("Dijite otro numero: "))

if num1 < num2:
    for i in range(num1,num2+1):
        print (i)
elif num2 < num1:
    for i in range(num2,num1+1):
        print (i)
else:
    ("Sus numeros son iguales o no son caracteres validos")
    