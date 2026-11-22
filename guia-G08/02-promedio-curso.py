# Promedio de curso
# Qué practica: Lista de diccionarios, acumulador y búsqueda del máximo

alumnos = [
    {"nombre":"Alejandro","nota":6.9},
    {"nombre":"Robert","nota":6.5},
    {"nombre":"Walter","nota":6.2},
    {"nombre":"Claudio","nota":3.9},
    {"nombre":"Felipe","nota":5.3},
    {"nombre":"Tómas","nota":4.5},
]

other_name = {"nombre":"Alejandro","nota":6.9}

#Imprime los nombres de los alumnos y sus notas
for alumno in alumnos:
    print(f"Alummo {alumno['nombre']} con un promedio: {alumno['nota']}")

#Ciclo para sumar notas y generar el promedio del curso 
notas_totales = 0
nota_mayor = 0
nombre_nota_mayor = ""

for i in alumnos:
    
   #Acumulador de notas
   notas_totales += i['nota'] # '+=' es decir notas_totales es = al total + nota
   
   #Buscar la nota mas alta
   if i['nota'] > nota_mayor:
       nota_mayor = i['nota']
       nombre_nota_mayor = i['nombre']
       
#Calcular Promedio
promedio_de_curso = notas_totales / len(alumnos)
   
#Mostrar resultados
print(f"El promedio del curso es de: {promedio_de_curso:.2f}") #:.2f es para que se muestren hasta dos decimales
print(f"El Estudiante con la nota mas alta fue: {nombre_nota_mayor} con una nota de {nota_mayor}")   


print(len(other_name))