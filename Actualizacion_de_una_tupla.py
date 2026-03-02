
frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")

frutas2= list(frutas) # transformo la tupla en lista
frutas2[1] = "Coco" #modifico la lista
frutas= tuple(frutas2) #transformo la lista en tupla

print(frutas)
#------------------------------------------------------------------------------------------------#
tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")

lista_frutas= list(tupla_frutas)

lista_frutas.append("Coco")

tupla_frutas = tuple(lista_frutas)

print(tupla_frutas)

#------------------------------------------------------------------------------------------------#
tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")
tupla_verduras=("Zanahoria","Ajo","Brocoli")

tupla_frutas +=tupla_verduras

print(tupla_verduras)
#------------------------------------------------------------------------------------------------#

tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")

lista_fruta=list(tupla_frutas)

lista_fruta.remove("Manzana")

tupla_fruta=tuple(lista_fruta)

print(tupla_fruta)