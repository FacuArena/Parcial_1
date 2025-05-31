def imprimir_matriz(matriz) -> list:
# -> ¿Qué hace?: Imprime una matriz mediante iteraciones con for.
# -> ¿Qué pide?: Solicita una matriz.
# -> ¿Qué retorna?: imprime una matriz.    
    for i in range(len(matriz)):     
        for j in range(len(matriz[i])):       
            print(matriz[i][j], end = "    ")
        print("\n----------------")
    return matriz

def cargar_matriz_notas(alumnos, examenes):
# -> ¿Qué hace?: Carga las notas de los alumnos por examenes declarados.
# -> ¿Qué pide?: Notas comprendidas entre 1 y 10.
# -> ¿Qué retorna?: Retorna una matriz.    
    matriz = []
    for i in range(alumnos):
        fila_temporal = []
        fila_temporal += [f"alumno_{i + 1}"]
        print(f"\nAlumno {i + 1}...")
        for j in range(examenes):
                while True:
                    try:
                        notas = int(input(f"Ingrese nota_{j + 1}: ")) 
                        if 1 <= notas <= 10:
                            fila_temporal += [notas]
                            break
                        else:
                             print("Ingrese una nota entre 1 y 10")
                    except ValueError:
                        print("ERROR!, ingrese un entero")
        matriz += [fila_temporal]
    return matriz

def porcentaje_aprobados(matriz) ->list:
# -> ¿Qué hace?: Calcula el porcentaje de examenes aprobados por alumno.
# -> ¿Qué pide?: solicita una matriz.
# -> ¿Qué retorna?: Una nueva matriz simplificando examenes por porcentaje total.    
    matriz_porcentajes = []
    for fila in matriz:
        alumno = fila[0]
        notas = fila[1:]
        total_de_notas = len(notas)
        nota_aprobada = 0
        for elemento in notas:
            if elemento >= 6:
                nota_aprobada += 1
        porcentaje_alumno = (nota_aprobada / total_de_notas) * 100
        matriz_porcentajes += [[alumno, porcentaje_alumno,"%"]]
    return matriz_porcentajes

def mejor_promedio(matriz):
# -> ¿Qué hace?: Calcula el promedio de notas por alumno.
# -> ¿Qué pide?: solicita una matriz.
# -> ¿Qué retorna?: Una nueva matriz de alumnos x promedio.
    matriz_promedio = []
    for i in matriz:
        alumno = i[0]
        notas = i[1:]
        total_de_notas = len(notas)
        total_alumno = 0
        for j in notas:
            total_alumno += j
        promedio = total_alumno / total_de_notas
        matriz_promedio += [[alumno, promedio]]
    return matriz_promedio

def buscar_nota(matriz, nota):
# -> ¿Qué hace?: Realiza una busqueda en la matriz.
# -> ¿Qué pide?: parametro matriz y nota.
# -> ¿Qué retorna?: Una nueva matriz de alumnos y examenes x nota buscada.
    resultado = []     
    for fila in range(len(matriz)):
        fila_momentanea = matriz[fila]
        alumno = fila_momentanea[0]
        for elemento in range(1, len(matriz[fila])):
            if matriz[fila][elemento] == nota:
                resultado += [[alumno, f"Examen {elemento}"]]
    return resultado