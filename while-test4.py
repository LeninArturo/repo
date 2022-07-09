#Prueba del operador or en el ciclo while

nombre=input('elige un mombre: ')
intentos=0

while (nombre=='lenin' or nombre=='jose' or nombre=='luis'):

    print(f'no puedes elegir {nombre} porque ya esta en uso')
    nombre=input('escribe otro nombre: ')
    
    if (nombre=='lenin'):
        print(f'te dije que {nombre} ya esta en uso ¿eres bruto?')
        nombre=input('escribe otro nombre: ')

    if (nombre=='jose'):
        print(f'te dije que {nombre} ya esta en uso ¿eres bruto?')
        nombre=input('escribe otro nombre: ')
       
    if (nombre=='luis'):
        print(f'te dije que {nombre} ya esta en uso ¿eres bruto?')
        nombre=input('escribe otro nombre: ')   
    

    if (nombre=='lenin'):
        print(f'si, definitivamente eres bruto')
        nombre=input('estoy cansado, puedes POR FAVOR escribir otro nombre?: ')
        
    if (nombre=='jose'):
        print(f'si, definitivamente eres bruto')
        nombre=input('estoy cansado, puedes POR FAVOR escribir otro nombre?: ')

    if (nombre=='luis'):
        print(f'si, definitivamente eres bruto')
        nombre=input('estoy cansado, puedes POR FAVOR escribir otro nombre?: ')


    if (nombre=='lenin' or nombre=='jose' or nombre=='luis'):
        print(f'si, definitivamente eres bruto, CHAO')
        break
else:
    print(f'ok te llamaras {nombre}')


print('termino el programa')