#Agenda usando una lista de diccionarios, donde cada contacto tenga nombre, teléfono y correo.

#Requisitos tecnicos:
#La búsqueda parcial debe usar el operador in sobre los nombres en minúscula (lower()).
#Debe manejarse el caso en que no se encuentren coincidencias, informando al usuario.
#El listado completo debe mostrarse ordenado alfabéticamente por nombre.

def menu():
    print('----------------------------')
    print('Bienvenido a la agenda Virutal')
    print('----------------------------')
    print('1. Agregar un contacto')
    print('2. Ordenar Agenda Alfabeticamente')
    print('3. Buscar contacto en la Agenda')
    print('----------------------------')
    print('----------------------------')
    

agenda = []

while True:
    
    menu()
    respuesta = int(input('Ingresa el numero de la opcion que deseas realizar: '))
    
    if respuesta == 1:
        nombre = input(('Ingresa el Nombre del contacto que deseas agregar: ')).lower()
        telefono=input(('Ingresa el numero telefonico del contacto que deseas agregar: ')).lower()
        correo = input(('Ingresa el Correo Electronico del contacto que deseas agregar: ')).lower()
        #Crear el diccionario con los datos solicitados
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'correo': correo
        }
        agenda.append(contacto)
    
    elif respuesta == 2:
        if agenda == []:
            print('No existen datos en la agenda')
        else:
            agenda_ordenada = sorted(agenda, key=lambda x: x['nombre'])
            print(agenda_ordenada)
    
    elif respuesta == 3:
        
        nombre_buscar = input('Ingresa el nombre que deseas buscar: ').lower()
        #Bandera que parte en False y si encuentra algo pasa a TRUE
        encontrado = False
        
        for i in range(len(agenda)):
            if nombre_buscar in agenda[i]['nombre']:
                print(f'Se ha encontrado una coincidencia con el nombre ingresado')
                print('----------------------------')
                print('----------------------------')
                print(f'Nombre: {agenda[i]['nombre']}')
                print(f'Telefono: {agenda[i]['telefono']}')
                print(f'Correo: {agenda[i]['correo']}')
                encontrado = True
        
        #Saliendo del Ciclo pregunto si encontro algo.
        if encontrado == False:
                print(f'No se encontro ningun resultado con {nombre_buscar}')
                
            
    elif respuesta == 4:
            print(agenda)
            
    elif respuesta == 0:
        print('----------------------------')
        print('----------------------------')
        print('Has salido del programa')
        print('----------------------------')
        print('----------------------------')
        
        break
        
            
    else:
        print('----------------------------')
        print('Ingresa una opcion valida')
        print('----------------------------')