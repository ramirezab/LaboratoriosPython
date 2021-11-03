#!/usr/bin/python3
Nombres_aprovados = []
while(True):

    a = input("Ingrese el nombre de la persona"
              " o bien ingrese salir para terminar\n")

    if a == "salir":
        break

    lista = a.split(' ')

    if len(lista) < 3 or len(lista) > 4:
        print("Por favor ingresar 3 o 4 componentes")

    else:
        mayus = []
        for x in lista:
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
