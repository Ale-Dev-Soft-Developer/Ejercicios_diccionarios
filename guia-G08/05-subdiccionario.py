# Subdiccionario
# Qué practica: Diccionarios anidados

cliente = {
    'nombre':'Alejandro',
    'rut':'207679739',
    'direcccion':{
        'calle': 'Los Cipreces',
        'numero':947,
        'comuna':'Machali',
        'region':'Ohiggins'}
}

print(f'El usuario {cliente['nombre']} de Rut: {cliente['rut']}, vive en la direccion: {cliente['direcccion']['calle']} #{cliente['direcccion']['numero']}, de la Comuna de {cliente['direcccion']['comuna']}, ubicada en la region de {cliente['direcccion']['region']}')