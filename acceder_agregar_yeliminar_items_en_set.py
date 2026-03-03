conjunto_frutas={"Manzana","Platano","Pera"}

# Los conjuntos no se pueden indexar ya que no tienen indice por ser no ordenados

for fruta in conjunto_frutas:
    print (fruta)

print("Manzana"in conjunto_frutas)
print("Banana"in conjunto_frutas)

conjunto_frutas.add("Banana") # Agrego elemento al conjunto

print(conjunto_frutas)

conjunto_tropical={"Piña","Mango","Papaya"}

# Agregar mas sets
conjunto_frutas.update(conjunto_tropical)

print(conjunto_frutas)

lista_frutas= ["Kiwi","Banana"]

# Puedo agregar cualquier estructura, ejemplo una lista

conjunto_frutas.update(lista_frutas)

print(conjunto_frutas)

# Eliminar elemento en conjunto

conjunto_frutas.remove("Banana")

print(conjunto_frutas)

# pop puede borrar elementos aleatoriamente ya que no hay orden

conjunto_frutas.pop()
print(conjunto_frutas)