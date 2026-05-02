"""def nombre_de_la_funcion(parametros):
    "Docstring de la funcion"
    #Cuerpo de la funcion
    # Puede contener una o mas lineas de codigo
    return "resultado"""

def suma (a,b):
    """Esta funcion suma dos numeros."""
    resultado= a + b
    return resultado

# 3 y 5 aca son los argumentos (valores)
resultado_suma = suma(3,5)
print (resultado_suma) # Output: 8

global_var= 10 # Variable global, accesible dentro y fuera de la funcion.

def mi_funcion():
    local_var= 20 # Variable local, accesible dentro de la funcion.
    print("Variable local dentro de la funcion:",local_var)
    print("Variable global dentro de la funcion:",global_var)

mi_funcion()
print("variable global fuera de la funcion:",global_var)