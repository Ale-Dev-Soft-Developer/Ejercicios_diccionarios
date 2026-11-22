# Valores de la UF
# Qué practica: Diccionario fecha → valor, conversión de formato y try / except

def ingresar_dato():
    
    try: 
        fecha = input("Ingresa la fecha en el formato 'dd-mm-aaaa':  ")
        valor_uf = input("Ingresa el valor de la uf: ")
    
        #Vuelvo el input normal a flotante para poder anotar la UF en formato original
        #Sino me genera un ValueError y me crashea el programa
        valor_uf = valor_uf.replace(".","")
        valor_uf = valor_uf.replace(",",".")
        valor_uf = float(valor_uf)
    
    
        diccionario_de_uf[fecha]= valor_uf
        
    except ValueError and TypeError:
        print("Hubo un error, intentalo de nuevo")
        
def comprobar_existencia_de_valor():
    comprobar_fecha = input("Ingresa la fecha que deseas comprobar si existe: ")
    
    try:
        if comprobar_fecha in diccionario_de_uf:
            #Se guarda el valor buscado en una variable para poder ocupar de manera directa.
            #Esto evita repetir codigo, mejora legibilidad.
            valor_actual_uf = diccionario_de_uf[comprobar_fecha]
        
            print(f"La fecha {comprobar_fecha} tiene ingresado un valor de: {valor_actual_uf}")
            cantidad_de_uf_a_calcular = int(input("Ingresa la cantidad de UF que desea calcular: "))
            resultado_valor_de_uf = cantidad_de_uf_a_calcular * valor_actual_uf
            print(f"El resultado de {valor_actual_uf} x {cantidad_de_uf_a_calcular} = {resultado_valor_de_uf}")
        else:
            print("La fecha que has ingresado no existe en los valores registrados.")
    except ValueError and TypeError:
        print("Ha ocurrido un error, vuelve a intentarlo.")
        
    



diccionario_de_uf = {}
print(diccionario_de_uf)
ingresar_dato()
comprobar_existencia_de_valor()
print(diccionario_de_uf)
