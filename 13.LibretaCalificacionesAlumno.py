def calificaciones():
    
    asignatura = input("Ingrese el nombre de la Asignatura: ").lower()
    
    if asignatura in (diccionario_notas):
        nota = input("Ingrese el promedio final de la asignatura: ")
        nota = nota.replace(",",".")
        nota = float(nota)
        diccionario_notas[asignatura]= nota
    else:
        print("Esta asignatura ya esta registrada.")
    

def actualizar_nota():
    
    try: 
        asignatura_actualizar = input("Ingrese el nombre de la asignatura para modificar la nota: ")
    
        if asignatura_actualizar in (diccionario_notas):
            nueva_nota = input("Ingrese el nuevo promedio final de la asignatura: ")
        
            nueva_nota = nueva_nota.replace(",",".")
            nueva_nota = float(nueva_nota)
        
            diccionario_notas[asignatura_actualizar] = nueva_nota
            print("\nSe ha actualizado con exito la nueva nota")
        else:
            print(f"\nLa asignatura {asignatura_actualizar} no existe, vuelve a intentarlo")
    except(ValueError):
        print("\nHas ingresado un valor invalido, recuerda usar caracteres, no numeros.")


def eliminar_asignatura():
    
    try:
        asignatura_eliminar = input("Ingresa el nombre de la asignatura que deseas eliminar: ")
    
        if asignatura_eliminar in diccionario_notas:
            del diccionario_notas[asignatura_eliminar]
        else:
            print(f"\nLa asignatira {asignatura_eliminar} no existe en el registro.")
    except(ValueError):
        print("\nHas ingresado un valor invalido, recuerda usar caracteres, no numeros.")
        

def calcular_promedio():
    
    if len(diccionario_notas) == 0:
        print("No hay datos suficientes para poder calcular el promedio")
        return
    
    notas_sumadas = sum(diccionario_notas.values())
    total_de_notas = len(diccionario_notas)
    operacion = notas_sumadas / total_de_notas
    
    print(f"\nEl promedio total de las notas es de: {operacion}")


def mostrar_diccionario():
    
    if len(diccionario_notas) == 0:
        print("\nNo hay datos suficientes para poder mostrar.")
        return
    
    lista_asignaturas = list(diccionario_notas.keys())
    
    for i in range(len(lista_asignaturas)):

        asignatura_actual = lista_asignaturas[i]
        nota_actual = diccionario_notas[asignatura_actual]
        print(f"\nAsignatura: {asignatura_actual} con promedio: {nota_actual}")
        
   
   
def menu():
    
    print("\n=========MENU===========")
    print("1. Agregar Asignatura")
    print("2. Actualizar Nota")
    print("3. Eliminar Asignatura")
    print("4. Calcular Promedio")
    print("5. Mostrar Diccionario")
    print("6. Salir del Programa")
    
   


diccionario_notas = {}


while (True):
    
    try:
        menu()
    
        respuesta = int(input("Ingresa la opcion numerica que deseas: "))
     
        if respuesta == 1:
            calificaciones()
        elif respuesta == 2:
            actualizar_nota()
        elif respuesta == 3:
            eliminar_asignatura()
        elif respuesta == 4:
            calcular_promedio()
        elif respuesta == 5:
            mostrar_diccionario()
        elif respuesta == 6:
            print("\nHas salido del programa")
            break

        
    except ValueError:
        print("\nIngresaste un dato invalido, la respuesta debe ser numerica.")
    