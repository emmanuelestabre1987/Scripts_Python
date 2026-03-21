diccionario={
    "nombre":"Emmanuel",
    "tecnologias":["python","javascript"],
    "ciudad":"San Marcos sierra",
    "profesion":"Licenciado en Logistica"
    
        }

# Copiar diccionario --> la mejor practica es la siguiente. Asi no se modifican ambos (original y copia)


diccionario2= diccionario.copy()

# o 

diccionario3= dict(diccionario)

print(diccionario2)
print(diccionario3)

# Recorrer con bucles
# For
for key in diccionario:
    print("clave:",key,"valor:",diccionario[key])

# Acceder al valor
for values in diccionario.values():
    print(values)

# Desempaquetar los items

for x,y in diccionario.items():
    print(x,y)