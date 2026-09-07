sistema = (
    {'clave':'idioma','valor':'Spanish'},
    {'clave':'moneda','valor':'CLP'},
    {'clave':'zona horaria','valor':'America/Santiago'},
    {'clave':'tema', 'valor':'Oscuro'}
)
    
while(True):    
    # try = intenta esto y si no resulta, ingresa al except
    try:
        print(f'las tuplas son inmutables por lo que si tratas de agregar algo no lo permitira.')
        print('Deseas agregar algo a la Tupla de Sistema?')
        respuesta = input('Ingresa Si o No: ').lower()
    
        if respuesta == 'si':
            clave = input('Ingresa la clave: ')
            valor = input('Ingresa el valor: ')
            dato = {
                'clave':clave,
                'valor': valor
            }
            sistema.append(dato)
        
        elif respuesta == 'no':
            print('Muy bien, entendiste lo que no se debe hacer')
            break
        else:
                print('------------------------------------------')
                print('Ingresa respuestas validas')
                print('------------------------------------------')
            
        #El except entra en juego solo cuando hay un error de Attribute
    except AttributeError as error:
        
        print('--------------ERROR--ERROR---------------')
        print('--------------ERROR--ERROR----------- ----')
        print('Has intentado agregar un dato a un tupla')
        print('--------------ERROR--ERROR---------------')
        print('------------------------------------------')
        print("AttributeError: 'tuple' object has no attribute 'append'")
        print('------------------------------------------')
        print('--------------ERROR--ERROR---------------')
        print('//////////Vuelve a intentarlo/////////////')
        print('--------------ERROR--ERROR---------------')
        print('--------------ERROR--ERROR---------------')