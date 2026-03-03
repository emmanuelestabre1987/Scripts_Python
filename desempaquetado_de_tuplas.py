from Actualizacion_de_una_tupla import tupla_fruta


tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")

# vamos a asignar estos elementos a variables
# No se puede desempaquetar solo una parte de la tupla
# Para eso tengo que elegir la cantidad de elementos a desempaquetar y poner uno mas con *
(a,b,c,*d) = tupla_fruta # Ejemplo aca solo quiero las primeras tres variables.

print(a)
print(b)
print(c)
print(d)

# Si necesito la primera y la ultima

(a,*b,c) = tupla_fruta # En este caso el * toma todo lo que no tiene una variable individual y lo empaqueta

print(a)
print(b)
print(c)