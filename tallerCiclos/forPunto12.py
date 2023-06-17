#12. Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

n = int(input("Ingrese la cantidad de estudiantes: "))

notaMaxima = float('-inf')  
notaMinima = float('inf')  
sumaNotas = 0  

for i in range(n):
    print("Estudiante", i + 1)
    sumaEstudiante = 0 

    for j in range(4):
        nota = float(input("Ingrese la nota: "))  

        sumaEstudiante += nota  

        if nota > notaMaxima: 
            notaMaxima = nota

        if nota < notaMinima:  
            notaMinima = nota

    promedioEstudiante = sumaEstudiante / 4  
    sumaNotas += sumaEstudiante  
    print(f"El promedio individual es: {promedioEstudiante}")

promedioTotal = sumaNotas / (n * 4) 
print("Dentro del curso, los siguientes promedios son: ")
print(f"La nota más alta es: {notaMaxima}")
print(f"La nota más baja es: {notaMinima}")
print(f"El promedio total es: {promedioTotal}")
