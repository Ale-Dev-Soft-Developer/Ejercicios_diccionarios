# Control de stock crítico
# Qué practica: Filtrar una lista de diccionarios y ordenarla con sorted() y lambda

def menu_bodega():
    print('------------------------------------------')
    print('Has ingresado al Menu de la Bodega Central')
    print('------------------------------------------')
    
    print('1. Mostrar Stock disponible de los productos ')
    print('0. Salir del programa ')
    print('Selecciona la opcion que deseas realizar: ')


control_de_stock = [
    {'nombre':'Mousepad', 'stock':6, 'stock_minimo':6},
    {'nombre':'Teclado', 'stock':42, 'stock_minimo':6},
    {'nombre':'Notebook', 'stock':2, 'stock_minimo':6},
    {'nombre':'Teclado Mecanico', 'stock':5,'stock_minimo':6},
]

while (True):
    
    try:
        menu_bodega()
        print('------------------------------------------')
        respuesta = int(input('Ingrese el numero de su respuesta: '))
        print('------------------------------------------')
        
        producto_con_stock_minimo = []
        contador_stock_minimo = 0
        stock_minimo_estado = False
        
        if respuesta == 1:
            for i in range(len(control_de_stock)):
                if control_de_stock[i]['stock'] <= control_de_stock[i]['stock_minimo']:
                    
                    producto_con_stock_minimo.append(control_de_stock[i])
                    contador_stock_minimo += 1
                    stock_minimo_estado = True
        
            # Ordenar de menor a mayor stock
            producto_con_stock_minimo = sorted(producto_con_stock_minimo, key= lambda producto: producto['stock'])
        
            if stock_minimo_estado == True:
                print(f"Encontre {contador_stock_minimo} productos que estan con el stock en minimo")
                print('------------------------------------------')
                print('Productos en Stock Minimo')
                print('------------------------------------------')
                for i in range(len(producto_con_stock_minimo)):
                    print('------------------------------------------')
                    print(f"Producto:{producto_con_stock_minimo[i]['nombre']}")
                    print(f"Stock:{producto_con_stock_minimo[i]['stock']}")
                    print(f"Stock minimo:{producto_con_stock_minimo[i]['stock_minimo']}")
                    print('------------------------------------------')
                
            elif stock_minimo_estado == False:
                print('No se ha encontrado productos con el stock minimo')
        
        elif respuesta == 0:
            print('------------------------------------------')
            print('Has salido del programa')
            print('------------------------------------------')
            break
        
        
        
    except ValueError:
        print('------------------------------------------')
        print('Has ingresado una respuesta en caracteres, recuerda usar solo numeros. Vuelve a intentarlo')
        print('------------------------------------------')