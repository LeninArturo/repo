#Prueba del operador or en el ciclo while

nombre=input('elige un mombre: ')

while nombre=='lenin' or nombre=='jose' or nombre=='luis':

    print(f'no puedes elegir {nombre} porque ya esta en uso')
    nombre=input('escribe otro nombre: ')

else:
    print(f'ok te llamaras {nombre}')

print('termino el programa')