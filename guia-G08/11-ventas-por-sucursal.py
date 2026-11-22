# Ventas por sucursal
# Qué practica: Acumulador, mejor elemento y formato de miles chileno

sucursales = (
    {
        'nombre_sucursal':'Carahue',
        'ventas_mes':12000000
    },
    {
        'nombre_sucursal':'Scranton',
        'ventas_mes':18000000
    },
    {
        'nombre_sucursal':'Beverly Hills',
        'ventas_mes':20000000
    },
    {
        'nombre_sucursal':'New York',
        'ventas_mes':16000000
    }
)


total_ventas_sucursales = 0
mejor_sucursal = sucursales[0]

for i in range (len(sucursales)):
    #Con este for recorro las sucursales y guardo en la variable sucursal_actual
    sucursal_actual = sucursales[i] 
    
    #Entro al valor de esa sucursal con sucursal_actual['ventas_mes']
    #Este += voy sumando el valor de cada sucursal y almacenandolo en la variable.
    total_ventas_sucursales += sucursal_actual['ventas_mes']
    
    #Comparo la sucursal actual con la mejor encontrada hasta el momento
    #Si la actual tiene más ventas, pasa a ser la nueva mejor sucursal
    if sucursal_actual['ventas_mes'] > mejor_sucursal['ventas_mes']:
        mejor_sucursal = sucursal_actual

#Paara chilenizar el monto
monto = f"{total_ventas_sucursales:,.0f}".replace("," , ".")
venta_chilena = f"{mejor_sucursal['ventas_mes']:,.0f}".replace("," , ".")

print(f"El total de ventas todas las Sucursales en este mes, fue de: ${monto}")
print(f"La sucursal con mas ventas fue {mejor_sucursal['nombre_sucursal']} con un monto total de: ${venta_chilena}")



#  :,.0f
# se lee asi:
# 1- : (aplica formato)   2- ,(separa a miles)  3- 0. (muestra 0 decimales y redondea el ultimo valor) 4- f(tratalo como numero decimal)