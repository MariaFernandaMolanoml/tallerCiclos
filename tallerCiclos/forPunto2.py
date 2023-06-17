#2. Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos 
n = int(input("Dijite un numero: "))

if n >=10:
    total= 1
    for multi in range(1,n + 1):
        total *= multi
    print(f"La multiplicacion de los {n} primeros numeros es: {total}")

else:
    if n >0 and n <10: 
        total=0
        for suma in range(1,n+1):
            total+=suma
        print(f"La suma de los {n} primeros numeros es: {total}")  
    else:
        print("Digite un numero y que sea positivo")   