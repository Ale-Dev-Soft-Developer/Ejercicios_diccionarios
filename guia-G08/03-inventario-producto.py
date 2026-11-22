# Inventario de un producto
# Qué practica: Menú para agregar, ver, actualizar y eliminar claves (pop, del)

def menu():
    print("1. Ingresar producto: ")
    print("2. Ver el inventario: ")
    print("3. Actualizar el inventario con un nuevo Producto: ")
    print("4. Eliminar producto: ")
    print("0. Finalizar programa ")

inventario = {}

while True:
    
    menu()
    respuesta = int(input('Ingresa el numero de la opcion que deseas realizar: '))
    if respuesta == 1:
        print('----------------------------')
        print('------INGRESAR PRODUCTO-----')
        print('----------------------------')
        nombre_producto = input('Ingresa el nombre del producto que deseas ingresar: ')
        stock_producto = int(input('Ingresa la cantidad del producto: '))
        precio_producto = int(input('Ingresa el precio unitario del producto sin punto ni coma: '))
        print('----------------------------')
        print('----------------------------')
        print('----------------------------')
        
        inventario['nombre']= nombre_producto
        inventario['stock']= stock_producto
        inventario['precio']= precio_producto
        print(f'Has ingresado el producto {inventario["nombre"]}, con un stock de {inventario["stock"]} y un precio de ${inventario["precio"]}')
    
    elif respuesta == 2:
        if inventario == {}:
            print('----------------------------')
            print('---------INVENTARIO---------')
            print('----------------------------')
            print('El inventario esta vacio')
            print('----------------------------')
            print('----------------------------')
            print('----------------------------')
        else:    
            print('----------------------------')
            print('---------INVENTARIO---------')
            print('----------------------------')
            if "stock" in inventario:
                print(f"El stock del producto {inventario['nombre']} es de: {inventario['stock']}")
            if "precio" in inventario:
                print(f"El precio del producto {inventario['nombre']} es de: {inventario['precio']}") 
                print('----------------------------')
                print('----------------------------')
                print('----------------------------')
            if not "stock" in inventario:
                print('----------------------------')
                print('----------------------------')
                print('No existe ningun registro de Stock que mostrar')
                print('----------------------------')
                print('----------------------------')
            if not "precio" in inventario:
                print('----------------------------')
                print('----------------------------')
                print('No existe ningun registro de Precio ingresado del producto')
                print('----------------------------')
                print('----------------------------')    
    elif respuesta == 3:
        if inventario == {}:
            print('----------------------------')
            print('---------INVENTARIO---------')
            print('----------------------------')
            print('El inventario esta vacio, no se puede actualizar ningun valor. Primero ingresa un producto')
            print('----------------------------')
            print('----------------------------')
            print('----------------------------')
        else:
            print('----------------------------')
            print('---------ACTUALIZAR---------')
            print('----------------------------')
            
            nombre_producto = input('Ingresa el nombre del producto que deseas ingresar: ')
            stock_producto = int(input('Ingresa la cantidad del producto: '))
            precio_producto = int(input('Ingresa el precio unitario del producto sin punto ni coma: '))
            
            inventario['nombre']= nombre_producto
            inventario['stock']= stock_producto
            inventario['precio']= precio_producto
        
    elif respuesta == 4:
        if inventario == {}:
            print('----------------------------')
            print('----ACTUALIZAR INVENTARIO---')
            print('----------------------------')
            print('El inventario esta vacio, no se puede actualizar ningun valor. Primero ingresa un producto')
            print('----------------------------')
            print('----------------------------')
            print('----------------------------')
        else:
            print('----------------------------')
            print('---------ELIMINAR---------')
            print('----------------------------')
            print('Que deseas eliminar?')
            print('1. Stock')
            print('2. Precio')
            print('3. Producto completo, dejar el inventario vacio')
            eleccion = int(input('Ingrese el numero de la opcion que desea escoger: '))
            if eleccion == 1:
                inventario.pop("stock")
                print('----------------------------')
                print('----------------------------')
                print('Se ha concretado su eleccion.')
                print('----------------------------')
                print('----------------------------')

            elif eleccion == 2:
                inventario.pop("precio")
                print('----------------------------')
                print('----------------------------')
                print('Se ha concretado su eleccion.')
                print('----------------------------')
                print('----------------------------')

            elif eleccion == 3:
                del(inventario)
                print('----------------------------')
                print('----------------------------')
                print('Se ha concretado su eleccion.')
                print('----------------------------')
                print('----------------------------')

            elif eleccion != 1 and eleccion != 2 and eleccion != 3:
                print('----------------------------')
                print('----------------------------')
                print('No has seleccionado una opcion correcta. Vuelve a intentarlo.')
                print('----------------------------')
                print('----------------------------')
    
    elif respuesta == 0:
        print('-------HAS SALIDO------')
        print('----------DEL----------')
        print('-------PROGRAMA--------')
        break