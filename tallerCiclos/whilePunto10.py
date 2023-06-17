#10. Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.
n = int(input("Ingrese la cantidad de estudiantes: "))

notaMaxima = float('-inf')
notaMinima = float('inf')
sumaNotas = 0

i = 0
while i < n:
    print("Estudiante", i + 1)
    sumaEstudiante = 0
    j = 0

    while j < 3:
        nota = float(input("Ingrese la nota: "))

        sumaEstudiante += nota

        if nota > notaMaxima:
            notaMaxima = nota

        if nota < notaMinima:
            notaMinima = nota

        j += 1

    promedioEstudiante = sumaEstudiante / 3
    sumaNotas += sumaEstudiante
    print(f"El promedio individual es: {promedioEstudiante}")

    i += 1

promedioTotal = sumaNotas / (n * 3)
print("Dentro del curso, los siguientes promedios son: ")
print(f"La nota más alta es: {notaMaxima}")
print(f"La nota más baja es: {notaMinima}")
print(f"El promedio total es: {promedioTotal}")
