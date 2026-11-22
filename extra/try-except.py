# Try / except
# Qué practica: Manejo de errores con try, except y finally

estado = True

while estado == True:
    try: 
        numero1 = int(input('Ingresa el primer numero: '))
        numero2 = int(input('Ingresa el segundo numero: '))
        resultado = numero1 + numero2
    except:
        print('Ingresa solo numeros, no letras')
        estado = False
    finally:

        print(f'El resultado de {numero1} + {numero2} = {resultado}')