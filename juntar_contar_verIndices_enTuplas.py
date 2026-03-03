tupla_frutas1=("Manzana","Uva","Fresa")
tupla_frutas2=("Mandarina", "Aguacate","Naranja","Kiwi")

tupla_frutas= tupla_frutas1 + tupla_frutas2

print(tupla_frutas)

# puedo duplicar una tupla con el *

tupla_frutas= tupla_frutas1 * 2 + tupla_frutas2

print(tupla_frutas)

print(tupla_frutas.count("Manzana"))

tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")
print(tupla_frutas.index("Uva"))