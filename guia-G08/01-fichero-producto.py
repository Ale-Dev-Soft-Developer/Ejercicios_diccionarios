# Fichero de producto
# Qué practica: Crear un diccionario y acceder a sus valores por clave

tienda = {
    "nombre":"Notebook",
    "precio":259.990,
    "stock":2,
    "categoria":"Computadores"
    }

print(f"De la categoria {tienda['categoria']} , esta disponible {tienda['nombre']}, que tiene un valor de ${tienda['precio']}, con un stock de {tienda['stock']} unidades disponibles")
