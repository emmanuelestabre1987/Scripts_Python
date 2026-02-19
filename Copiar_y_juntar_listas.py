frutas= ["Manzana", "Platano", "Pera", "Mandarina", "Fresa", "Piña" ]

copia_frutas= frutas.copy()
copia2_frutas= list(frutas)

print(copia_frutas)

# Juntar listas

frutas1= ["Manzana", "Platano", "Pera"]
frutas2= ["Mandarina", "Fresa", "Piña"]

frutas= frutas1 + frutas2

frutas1.extend(frutas2)

print(frutas1)

print(frutas.count("Manzana"))

