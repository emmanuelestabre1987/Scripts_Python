"""def saludar(nombre, apellido = "Estabre"): # En este caso nombre y apellido son argumentos. Con el igual hago que no sea obligatorio el parametro.
    print("Hola", nombre, apellido)

saludar("Emmanuel", "Estabre") # Esto hace que se ejecute
"""

"""def saludar(*nombres): # El asterisco se pone cuando no sabemos la cantidad de argumentos que van a entrar
    print("Hola", nombres[0], nombres[1])

saludar("Emmanuel", "Estabre") # Esto hace que se ejecute""" # Tenemos que asegurarnos de recibir la misma cantidad de argumentos que el parametro

"""def saludar(*nombres): # El asterisco se pone cuando no sabemos la cantidad de argumentos que van a entrar
    if len(nombres) > 0:
        print("Hola", nombres[0], nombres[1])
    else:
        print("Hola", nombres[0])

saludar("Emmanuel", "Estabre")"""

"""def padre_orgulloso(nene1,nene3,nene2):
    print("Mis hijos son:",nene1,nene2,"y",nene3)
    print("Y el mas pequeño es nene3")

padre_orgulloso(nene1= "Ricardito", nene2= "Nicolas",nene3= "Juancito" )# Keywords Arguments correcto"""
"""padre_orgulloso( "Ricardito", "Nicolas","Juancito" )""" # Esto no

def padre_orgulloso(**nenes):
    print("Mis hijos son:",nenes["a"],nenes["b"],"y",nenes["c"])
    print("Y el mas pequeño es", nenes["c"])

    padre_orgulloso(a = "Ricardito", b= "Nicolas",c= "Martin")