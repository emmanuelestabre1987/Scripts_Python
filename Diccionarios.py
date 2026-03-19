#------------------
# DICCIONARIO [Coleccion no ordenada de pares clave-valor]
#------------------
diccionario={
    "nombre":"Emmanuel",
    "tecnologias":["python","javascript"],
    "ciudad":"San Marcos sierra",
    "profesion":"Licenciado en Logistica"
    
        }
# Acceder a los valores
nombre=diccionario.get("nombre")

# Acceder a las claves
claves= diccionario.keys()

# Agregar clave/valor a diccionario, se pone una clave que no existia
diccionario["primo"]= "Mariano Calvo"

# Traer los valores
valores=diccionario.values()

# Traer items --> trae una lista de tuplas de clave valor.
items=diccionario.items()

print(claves)
print(diccionario)
print(valores)
print(items)

if "nombre" in diccionario:
    print("exite la clave nombre")