#!/usr/bin/python3

#Bryan Ramírez Ampié B35581

#Lista que almaceará los nombres corregidos
Nombres_aprovados = []

#Ciclo para ingresar los nombres
while(True):

    a = input("Ingrese el nombre de la persona"
              " o bien ingrese salir para terminar\n")

    #Coprobación de input para cerrar programa
    if a == "salir":
        break

    lista = a.split(' ')

    #comprobación de cantidad de elementos igresados
    if len(lista) < 3 or len(lista) > 4:
        print("Por favor ingresar 3 o 4 componentes")

    else:
        mayus = [] #Lista para almacenar los nombres temporalmente
        for x in lista:
            
            #Se comprueba si todos los componenetes ingresado son str
            if x.isalpha() is False:
                print("Por favor no ingresar números con el nombre")
                mayus = []
                break
            else:
                mayus.append(x.capitalize())

        nombre = ' '.join(mayus)
        Nombres_aprovados.append(nombre)
        


for nom in Nombres_aprovados:
    print(nom)
