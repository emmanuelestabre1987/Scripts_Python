tupla_frutas=("Manzana","Uva","Fresa","Mandarina", "Aguacate","Naranja","Kiwi")

for fruta in tupla_frutas:
    print(fruta)

for i in range(len(tupla_frutas)):
    print(tupla_frutas[i], "con el indice",i)

i= 0

while i < len(tupla_frutas):
    print(tupla_frutas[i])
    i +=1