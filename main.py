from parcial import *
def main():
    alumnos = None
    examenes = None
    matriz = None            
    while True:
        print("\n--------MENU PRINCIPAL------\n" \
        "1_ Cargar cantidad de alumnos y examenes\n" \
        "2_ cargar matriz notas"
        "3_ Imprimir grilla\n" \
        "4_ Porcentaje\n" \
        "5_ proimedio\n" \
        "6_ buscar nota" \
        "7_ salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                while True:
                    try:
                        print("\n --- INGRESAR CANTIDAD DE ALUMNOS Y EXAMENES ---\n")
                        alumnos = int(input("Ingrese cantidad de alumnos: "))
                        if alumnos <= 0:#validamos
                            print("No haz cargado nada..")
                            continue #volvemos al bucle

                        examenes = int(input("Ingrese cantidad de examenes: "))
                        if examenes <= 0: #validamos 
                            print("No haz cargado nada..")
                            continue #volvemos al bucle

                        break #Saliendo...
                    except ValueError:
                        print("ERROR!") 

            case 2:
                #Consultamos si se cargo almnos y examenes
                if alumnos is not None and examenes is not None:
                    print("\n---INGRESAR NOTAS DE EXAMENES POR ALUMNO, (1 A 10)\n")
                    matriz = cargar_matriz_notas(alumnos, examenes)
                else:
                    print("Debe cargar alumnos y examenes")
            case 3:
                    #no imprimira la matriz si no fue cargada previamente
                if matriz == None:
                    print("\nMatriz vacia :/")
                else:
                    #imprimira esa matriz de a x e
                    print("\n-------------------------")
                    imprimir = imprimir_matriz(matriz)
            case 4:
                    #no imprimira la matriz si no fue cargada previamente
                if matriz == None:
                    print("\nMatriz vacia :/") 
                else: 
                    #imprime el porcentaje de examenes aprobados por alumno, devolviendo una nueva matriz              
                    print("Porcentaje decada alumno en relacion a sus examenes aprobados..\n")
                    llamada_funcion = porcentaje_aprobados(matriz)
                    imprimir_matriz(llamada_funcion)
                    print()
            case 5:
                #si no tenemos matriz cargada no la va a tratar de imprmir
                if matriz == None:
                    print("\n Matriz vacia :/")
                else:
                    #si tenemos una matriz cargada la imprimimos con el promedio
                    print("Promedio de cada alumno\n")
                    imprimir_matriz(mejor_promedio(matriz))
            case 6:
                #Solicita una nota para ingresarla a la funcion buscar nota
                print("Ingrese una nota para buscarla en la matriz de alumnos")
                nota = int(input("Nota: "))
                imprimir_matriz(buscar_nota(matriz, nota))
            
            case 7:
                print("Cerrando programa..")
                break 
main()       