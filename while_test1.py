#Prueba del ciclo while y el salto de linea \n

nombre=input('\nElige un mombre: ')

while nombre=='lenin':

    print(f'\nNo puedes elegir {nombre} porque ya esta en uso')
    nombre=input('\nEscribe otro nombre: ')

print(f'\nOk te llamaras {nombre}')

print('\nTermino el programa\n')