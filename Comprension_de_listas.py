frutas= ["Manzana", "Platano", "Pera", "Mandarina", "Fresa", "Piña" ]
frutas_con_e=[]

for fruta in frutas:
    if "e" in fruta:
        frutas_con_e.append(fruta)

#             dato a              
#             asignar    bucle           condicion

frutas_sin_mandarina= [fruta for fruta in frutas if fruta != "Mandarina"]
print(frutas_sin_mandarina)

frutas2= [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]

print(frutas2)