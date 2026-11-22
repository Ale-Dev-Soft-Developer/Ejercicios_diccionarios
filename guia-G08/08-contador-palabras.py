# Contador de palabras
# Qué practica: split(), get() y ordenar items() por valor

diccionario = {}

frase = input("Que frase deseas ingresar?: ").lower()
palabra = frase.split()

#recorre la lista 
for i in range(len(palabra)):
    #get() busca la palabra en el diccionario y si la encuentra la suma y guarda en el contador de nuevo_diccionario.
    nuevo_diccionario = diccionario.get(palabra[i],0) +1
    #Si la palabra no existe se crea.
    #Si existe se reemplaza el viejo valor por el nuevo
    diccionario[palabra[i]] = nuevo_diccionario

#Metodo de lambda para ordenar el diccionario de mayor a menor
diccionario_ordenado = sorted(
    diccionario.items(),
    #lambda item indica que el ordenamiento sera por el item[1] es decir por el valor.
    key=lambda item: item[1],
    #reverse True para que cuente de mayor a menor
    reverse=True
    )


print(diccionario_ordenado)