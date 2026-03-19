#------------------
# DICCIONARIO [Coleccion no ordenada de pares clave-valor]
#------------------
diccionario={
    "nombre":"Emmanuel",
    "tecnologias":["python","javascript"],
    "ciudad":"San Marcos sierra",
    "profesion":"Licenciado en Logistica"
    
        }
# Actualizar datos en diccionarios
diccionario.update({"nombre":"Ricardo Rodriguez", "edad":25})
print(diccionario)

# Agregar datos
diccionario["Estado_civil"]="casado"
diccionario.update({"nombre_del_perro":"Fatima"})

# Borrar datos con clave
diccionario.pop("profesion")
del diccionario["nombre"]

# Eliminar el ultimo item del diccionario

diccionario.popitem()

# Limpiar diccionario
diccionario.clear()
