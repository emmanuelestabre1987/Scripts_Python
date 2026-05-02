"""def mostrar_mercaderia(mercaderia):
    for item in mercaderia:
        print(item)

lista_frutas = ["Manzana", "Pera","Platano"]

mostrar_mercaderia(lista_frutas) """

# Veamos como retornar algo

"""def suma(a,b):
    return a + b

print(suma(2,3))"""

"""def suma(a,b):
    resultado= a + b
    return resultado

print(suma(2,3))"""

"""def suma(a,b):
    resultado= a + b # Variable local (solo disponible dentro de la funcion)
    return resultado

resultado= suma(2,3) # Variable global (disponible de forma global)

print(resultado) """

def suma(a,b): # Argumentos posicionales
    """Esta funcion sumara los dos argumentos que se pasen"""
    pass # Permite que no se rompa el codigo y no haga nada

resultado= suma(a=2, b= 3) # Variable global (disponible de forma global) + keywords Arguments

print(resultado)

def devolver_cuadrado_1(x, /): # Con el , / no permite Keyword Argument.
    """ Devuelve el cuadrado del argumento pasado"""
    return x**2
print(devolver_cuadrado_1(2))

def devolver_cuadrado_2(*, x): # Con el *, Solo acepta keyword argument
    """ Devuelve el cuadrado del argumento pasado"""
    return x**2
print(devolver_cuadrado_2(x = 2))

# Mixto
def calcular_resultado(a,b ,/,*,c,d): # De la barra para atras solo son posicion arguments, del asterisco en adelante keywords arguments.
    print(a + b + c + d)

calcular_resultado(1,2,c = 3,d = 4)

def operaciones(a,b):
    suma= a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return[suma,resta,multiplicacion,division]

print(operaciones(4,2))