def crear_matriz_alumnos():
    print("\n --- INGRESAR CANTIDAD DE ALUMNOS Y EXAMENES ---\n")
    alumnos = int(input("Ingrese cantidad de alumnos: "))
    examenes = int(input("Ingrese cantidad de examenes: "))
    print("\n---INGRESAR NOTAS DE EXAMENES, (1 A 10)\n")
    return cargar_matriz_notas(alumnos, examenes) 

def cargar_matriz_notas(alumnos = 2, examenes = 3 ):
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

def imprimir_matriz(matriz) -> list:
    for i in range(len(matriz)):     
        for j in range(len(matriz[i])):       
            print(matriz[i][j], end = "    ")
        print("\n----------------")
    return matriz


def porcentaje_aprobados(matriz) ->list:
    matriz_porcentajes = []
    for fila in matriz:
        alumno = fila[0]
        notas = fila[1:]
        total_de_notas = len(notas)
        alumnos_aprobados = 0
        for elemento in notas:
            if elemento >= 6:
                alumnos_aprobados += 1
        porcentaje_alumno = (alumnos_aprobados / total_de_notas) * 100
        matriz_porcentajes += [[alumno, porcentaje_alumno,"%"]]
    return matriz_porcentajes


matriz = []            
while True:
    print("--------MENU PRINCIPAL------\n" \
    "1_ Cargar cantidad de alumnos y examenes\n" \
    "2_ Imprimir grilla\n" \
    "3_ Porcentaje\n" \
    "0_ Cerrar programa..\n")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            print("Ingrese numero de alumnos y cantidad de examenes (Por default hay 2 alumnos y 3 examenes cargados)")
            matriz = crear_matriz_alumnos()
        case 2:
            print("\n-------------------------")
            imprimir = imprimir_matriz(matriz)
        case 3:
            print("Porcentaje decada alumno en relacion a sus examenes aprobados..\n")
            llamada_funcion = porcentaje_aprobados(matriz)
            imprimir_matriz(llamada_funcion)
            print()
        case 0:
            print("Cerrando programa..")
            break        