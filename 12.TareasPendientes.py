def menu():

    print("\n===== GESTOR DE TAREAS =====")

    print("1. Agregar tarea")

    print("2. Marcar tarea como completada")

    print("3. Mostrar tareas")

    print("4. Salir")
    
def agregar_tarea():
    
    descripcion = input("Ingresa la descripcion de la Tarea: ")
    
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas_agregadas.append(tarea)
    print("Tarea agregada con exito")
    

def marcar_completada():
    if len(tareas_agregadas) == 0:
        print("No existe tareas registradas")
        return
    
    for i in range(len(tareas_agregadas)):
        estado = "✔" if tareas_agregadas[i]["completada"] else "✘"
        print(f"{i}. {tareas_agregadas[i]['descripcion']} [{estado}]")
    
    try:
        indice = int(input("Ingrese el número de la tarea que desea completar: "))
        # Validar que el índice exista
        if indice >= 0 and indice < len(tareas_agregadas):
            tareas_agregadas[indice]["completada"] = True
            print("La tarea fue marcada como completada.")

        else:
            print("El índice ingresado no existe.")
            
    except ValueError:
        print("Debe ingresar un número.")
    
    
def mostrar_tareas(): 
    # Comprensión de lista para obtener únicamente las tareas pendientes

    tareas_pendientes = [tarea for tarea in tareas_agregadas if tarea["completada"] == False]

    # Comprensión de lista para obtener únicamente las tareas completadas

    tareas_completadas = [ tarea for tarea in tareas_agregadas if tarea["completada"] == True]
    

    print("\n===== TAREAS PENDIENTES =====")

    if len(tareas_pendientes) == 0:

        print("No existen tareas pendientes.")

    else:

        for i in range(len(tareas_pendientes)):

            print(f"- {tareas_pendientes[i]['descripcion']}")

    print("\n===== TAREAS COMPLETADAS =====")

    if len(tareas_completadas) == 0:

        print("No existen tareas completadas.")

    else:

        for i in range(len(tareas_completadas)):

            print(f"- {tareas_completadas[i]['descripcion']}")
    
    
    
tareas_agregadas = []
tareas_pendientes = []
tareas_completadas = []


while True:

    menu()

    try:

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            agregar_tarea()

        elif opcion == 2:

            marcar_completada()

        elif opcion == 3:

            mostrar_tareas()

        elif opcion == 4:

            print("Programa finalizado.")

            break

        else:

            print("Opción no válida.")

    except ValueError:

        print("Debe ingresar un número.")




tareas_completadas_a = []
tareas_no_completadas= []

for i in range(len(tareas_agregadas)):
    
    tarea_actual = tareas_agregadas[i]
    
    if tarea_actual['completada'] == True:
        tareas_completadas_a.append(tarea_actual)
    elif tarea_actual['completada'] == False:
        tareas_no_completadas.append(tarea_actual)
        
        

