#5. Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
numeroFacturas = int(input("Ingrese el número de facturas (0 para finalizar): "))
total = 0

while numeroFacturas > 0:
    monto = float(input("Ingrese el monto de la factura (0 para finalizar): "))
    total += monto
    numeroFacturas -= 1

    if monto == 0:
        print("Proceso finalizado")
        break

if total >= 1 and total <= 999:
    print("Total a pagar:", total)
elif total > 1000:
    descuento = total * 0.1
    total -= descuento
    print("Total a pagar:", total)
else:
    if numeroFacturas == 0:
        print("Proceso finalizado")
