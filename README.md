# Ejercicios de diccionarios en Python 🐍

Ejercicios de lógica de programación con **diccionarios** en Python. Parten creando y leyendo un diccionario simple y llegan a programas completos con menú, donde se agregan, buscan, actualizan y eliminan datos.

Los hice mientras estudio **Analista Programador en INACAP**, a partir de la guía de diccionarios del curso (G08).

## ¿Cómo ejecutarlos?

Necesitas **Python 3.12 o superior** (algunos ejercicios usan comillas anidadas dentro de f-strings, que se permiten desde esa versión). Desde la carpeta del repositorio:

```bash
python3 guia-G08/01-fichero-producto.py
```

La mayoría de los ejercicios piden datos por teclado con `input()`.

## 📘 Guía G08

### Crear diccionarios y acceder a sus datos

| # | Ejercicio | Qué practica |
|---|-----------|--------------|
| 01 | [Fichero de producto](guia-G08/01-fichero-producto.py) | Crear un diccionario y acceder a sus valores por clave |
| 05 | [Subdiccionario](guia-G08/05-subdiccionario.py) | Diccionarios anidados |
| 06 | [Tupla de diccionarios](guia-G08/06-tupla-de-diccionarios.py) | Inmutabilidad de las tuplas y manejo de `AttributeError` |

### Recorrer, calcular y ordenar

| # | Ejercicio | Qué practica |
|---|-----------|--------------|
| 02 | [Promedio de curso](guia-G08/02-promedio-curso.py) | Lista de diccionarios, acumulador y búsqueda del máximo |
| 07 | [Control de stock crítico](guia-G08/07-control-stock-critico.py) | Filtrar y ordenar con `sorted()` y `lambda` |
| 08 | [Contador de palabras](guia-G08/08-contador-palabras.py) | `split()`, `get()` y ordenar `items()` por valor |
| 11 | [Ventas por sucursal](guia-G08/11-ventas-por-sucursal.py) | Acumulador, mejor elemento y formato de miles chileno |

### Programas con menú

| # | Ejercicio | Qué practica |
|---|-----------|--------------|
| 03 | [Inventario de un producto](guia-G08/03-inventario-producto.py) | Agregar, ver, actualizar y eliminar claves (`pop`, `del`) |
| 04 | [Agenda de contactos](guia-G08/04-agenda-contactos.py) | Búsqueda parcial con `in` y orden alfabético |
| 09 | [Nómina de empleados](guia-G08/09-nomina-empleados.py) | Filtro por rango y orden de mayor a menor |
| 10 | [Valores de la UF](guia-G08/10-valores-uf.py) | Diccionario fecha → valor y conversión de formato |
| 12 | [Gestor de tareas](guia-G08/12-tareas-pendientes.py) | Estados booleanos y comprensión de listas |
| 13 | [Libreta de calificaciones](guia-G08/13-libreta-calificaciones.py) | CRUD sobre un diccionario y `values()` para el promedio |
| 14 | [Catálogo de libros](guia-G08/14-catalogo-libros.py) | Búsqueda parcial, control de duplicados y disponibilidad |
| 15 | [Horario semanal de clases](guia-G08/15-horario-semanal-clases.py) | 🚧 Pendiente |

## ➕ Extra

| Ejercicio | Qué practica |
|-----------|--------------|
| [Try / except](extra/try-except.py) | Manejo de errores con `try`, `except` y `finally` |

## Autor

**Alejandro Gutiérrez Bustamante**, estudiante de Analista Programador (INACAP).
