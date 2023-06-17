# 1. Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos
n = int(input("Dijite un numero: "))

if n >= 10:
    total = 1
    multi = 1
    while multi <= n:
        total *= multi
        multi += 1
    print(f"La multiplicacion de los {n} primeros numeros es: {total}")

else:
    if 0 < n < 10:
        total = 0
        suma = 1
        while suma <= n:
            total += suma
            suma += 1
        print(f"La suma de los {n} primeros numeros es: {total}")
    else:
        print("Digite un numero y que sea positivo")
