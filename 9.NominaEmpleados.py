def menu():
    print("1. Ingresar un nuevo empleado")
    print("2. Buscar por trabajador por rango de Dinero")
    print("3. Ordenar trabajadores por sueldo de Mayor a menor")

def agregar_empleado():
    print("----- Has ingresado a la opcion de Agregar empleado -----")
   
    nombre = input(f"Ingrese el nombre del empleado: ")
    cargo = input(f"Ingrese el cargo del empleado: ")
    sueldo = int(input(f"Ingrese el sueldo del empleado: "))
    
    empleado = {
        'nombre':nombre,
        'cargo': cargo,
        'sueldo':sueldo
    }
    empleados.append(empleado)

def filtro_por_rango_de_sueldo():
    print("----- Has ingresado a la busqueda filtrada por rango -----")
    if len(empleados) == 0:
        print("No se han ingresado datos como para poder filtrar datos.")
    
    else: 
        minimo = int(input("Ingresa el monto minimo: "))
        maximo = int(input("Ingresa el monto maximo: "))
    
        for i in range(len(empleados)):
            if empleados[i]['sueldo'] >= minimo and empleados[i]['sueldo'] <= maximo:
                print(f"En el rango de: {minimo} y {maximo}")
                print(f"El Empleado {empleados[i]['nombre']} tiene un sueldo de: {int(empleados[i]['sueldo'])} ")
    
def sueldo_mayor_a_menor():
    if len(empleados) == 0:
        print("No se han ingresado datos como para poder ordenar sueldos.")
    
    else:
        sueldos_ordenados = sorted(
        empleados,
        key=lambda item:item['sueldo'],
        reverse=True
    )
    return print(sueldos_ordenados)

    
    
empleados = []

while (True):
    menu()
    try:
        respuesta = int(input("Ingresa el numero de las opciones que deseas realizar: "))
        
        if respuesta == 1:
            agregar_empleado()
        
        elif respuesta == 2:
            filtro_por_rango_de_sueldo()
        
        elif respuesta == 3:
            sueldo_mayor_a_menor()
        
        elif respuesta == 0:
            print("Hasta la vista Baby!!")
            break
    except ValueError:
        print("Recuerda ingresar una respuesta numerica. Vuelve a intentarlo")