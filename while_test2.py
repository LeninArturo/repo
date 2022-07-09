#Prueba del else en el ciclo while

nombre=input('Elige un mombre: ')

while nombre=='lenin':

    print(f'No puedes elegir {nombre} porque ya esta en uso')
    nombre=input('Escribe otro nombre: ')

else:
    print(f'Ok te llamaras {nombre}')

print('Termino el programa')