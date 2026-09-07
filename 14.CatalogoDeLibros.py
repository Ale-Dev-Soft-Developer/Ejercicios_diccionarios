def agregar_libros():
        
        nombre_libro = input("Ingresa el nombre del libro: ").lower()
        autor_libro = input("Ingresa el nombre del autor del libro: ").lower()
        
        for i in range(len(biblioteca)):
            libro_actual = biblioteca[i]
            if nombre_libro == libro_actual["titulo"] and autor_libro == libro_actual["autor"]:
                print(f"El libro '{libro_actual['titulo']}' del autor {libro_actual['autor']} ya se ha ingresado al sistema, no se puede volver a ingresar.")
                return
         
        ano_libro = input("Ingresa el año en el que fue publicado el libro: ")
        
        
        libro = {
            "titulo":nombre_libro,
            "autor":autor_libro,
            "ano":ano_libro,
            "disponibilidad": True
        }
        biblioteca.append(libro)
             
  
    

def buscar_libro():
    
        if len(biblioteca) == 0:
            print("No hay datos suficientes para realizar la busqueda")
            return
        
        libros_de_autor = input("\nIngrese el nombre del Autor: ").lower()
        libros_encontrados= []
        
        for i in range(len(biblioteca)):
            autor_actual = biblioteca[i]
        
        #Utilizo el IN para poder hacer una busqueda con coincidencia parcial.
        #Busca con la palabra ingresada alguna coincidencia en los valores ingresados
            if libros_de_autor in autor_actual['autor']:
                libros_encontrados.append(autor_actual['titulo'])
        
        if len(libros_encontrados) == 0:
            print(f"No se han encontrado resultados con el nombre: {libros_de_autor} ")
        else: 
            print(f"Los libros encontrados del Autor: {libros_de_autor}")
            for i in range(len(libros_encontrados)):
                print(f"- {libros_encontrados[i]}")
     
    

def marcar_libro():
    if len(biblioteca) == 0:
        print("\nNo hay datos suficientes para realizar esta accion")
        return
    
    libros_disponibles.clear()
    
    for i in range(len(biblioteca)):
        libro_actual = biblioteca[i]
        
        if libro_actual['disponibilidad'] == True:
            libros_disponibles.append(libro_actual)
            
    #Imprimo los libros disponibles si es que hay
    print(f"Los libros disponibles para prestamo son: ")
    for i in range(len(libros_disponibles)):
        libro_disponible = libros_disponibles[i]
        print(f" {i}. '{libro_disponible['titulo']}' del autor: {libro_disponible['autor']}")
        
    #Imprimo los libros prestados si es que hay    
    print(f"\nLos libros NO disponibles para prestamo son: ")
    if len(libros_prestados) == 0:
        print("No hay libros prestados.")
    else:
        for i in range(len(libros_prestados)):
            libro_prestado = libros_prestados[i]
            print(f" - '{libro_prestado['titulo']}' del autor: {libro_prestado['autor']}")
    
    try:
        libro_a_prestar = int(input("\nIngresa el numero del libro que deseas marcar como prestado: "))
        
        if libro_a_prestar >= 0 and libro_a_prestar < len(libros_disponibles):
            libro_seleccionado = libros_disponibles[libro_a_prestar]
            libro_seleccionado['disponibilidad'] = False
            libros_prestados.append(libro_seleccionado)
            print(f"Has seleccionado el libro '{libro_seleccionado['titulo']}' del autor: {libro_seleccionado['autor']}")
        
    except(ValueError):
        print("\nHas ingresado un valor incorrecto, se esperaba una respuesta numerica.")
            
        
    

def mostrar_catalogo():
    
    if len(biblioteca) == 0:
        print("\nNo es posible mostrar datos ya que la Biblioteca se encuentra vacia.")
        return
    
    for i in range(len(biblioteca)):
        libro = biblioteca[i]
        
        if libro['disponibilidad'] == True:
            print(f"El libro '{libro['titulo']}' del autor '{libro['autor']}', escrito en el año {libro['ano']}. Esta disponible para prestamo. ")
        elif libro['disponibilidad'] == False:
            print(f"El libro '{libro['titulo']}' del autor '{libro['autor']}', escrito en el año {libro['ano']}. *NO* disponible para prestamo. ")
                
    

def menu():
    
    print("\n=========MENU===========")
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Marcar Libro como prestado")
    print("4. Mostrar Catalogo ordenado por año")
    print("5. Salir del Programa")
    

biblioteca = []
libros_prestados = []
libros_disponibles = []

while (True):
    
    try:
        menu()
    
        respuesta = int(input("Ingresa la opcion numerica que deseas: "))
     
        if respuesta == 1:
            agregar_libros()
        elif respuesta == 2:
            buscar_libro()
        elif respuesta == 3:
            marcar_libro()
        elif respuesta == 4:
            mostrar_catalogo()
        elif respuesta == 5:
            print("\nHas salido del programa")
            break

        
    except ValueError:
        print("\nIngresaste un dato invalido, la respuesta debe ser numerica.")