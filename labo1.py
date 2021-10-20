#!/usr/bin/python3

char = input('Ingrese el caracter de la pirámide ')
while True:

    try:
        itera = int(input('Ingrese el tamaño de la base de la pirámide '))
        break
    except:
        print('El valor ingresado no es válido, por favor ingrese un número entero ')

for x in range (itera+1):

    
    print (x*char)
