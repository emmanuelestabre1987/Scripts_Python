conjunto_letras={"a","b","c"}
conjunto_numeros={1,2,3}

union= conjunto_letras.union(conjunto_numeros)

print(union)

union2= conjunto_letras | conjunto_numeros

print(union2)

conjunto_letras2={"d","e","f"}
tupla_numeros=(4,5,6)

union3= conjunto_letras2.union(tupla_numeros) # Si es otra estructura como una tupla hay que utilizar "union"
print(union3)

union4 = conjunto_letras.update(tupla_numeros)

print(union4)

set_tecnologia_universidad_chicago={"python","javascript","AWS"}
set_tecnologia_universidad_oxford={"python","Typescript","GoogleCloud"}

set3= set_tecnologia_universidad_chicago.intersection(set_tecnologia_universidad_oxford) # veo la interseccion de dos conjuntos

print(set3)

set4= set_tecnologia_universidad_chicago & set_tecnologia_universidad_oxford # Con este simbolo tambien veo interseccion

print(set4)

set_tecnologia_universidad_chicago.intersection_update(set_tecnologia_universidad_oxford) # Hago un update del primero con el segundo
print(set_tecnologia_universidad_chicago)

# Si en vez de interseccion quiero diferencia.

set5= set_tecnologia_universidad_chicago.difference(set_tecnologia_universidad_oxford)

print(set5)

# O

set6= set_tecnologia_universidad_oxford - set_tecnologia_universidad_chicago

print(set6)

# Bucles - Unica forma de recorrer el set es for, ya que no tiene indice.

conjunto_verduras= {"Lechuga","Tomate","Batata"}

for verdura in conjunto_verduras:
    print(verdura)

# copiar conjunto

conjunto_copia = conjunto_verduras.copy()
print(conjunto_copia)