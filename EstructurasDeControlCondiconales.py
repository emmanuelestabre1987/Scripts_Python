# if,elif,else

x = 10

if x > 0:
    print("X es un numero positivo")
elif x < 0:
    print("X es un numero negativo")
else:
    print("X es igual a 0")


visa= True
pasaporte= True

if visa and pasaporte:
    print("Puede ingresar a cualquier pais")
elif pasaporte and not visa:
    print("Puedes ingresar solo a los paises que no requieren visa")
else:
    print("Debes conseguir la documentacion antes de viajar")

edad=61

if edad < 18 or edad > 60:
    if edad < 18:
        print("No puedes ingresar a la disco")
    else:
        print(" Por una cuestion de seguridad no se permite ingreso a mayores de 60 años")
elif edad >= 18 and edad <= 60:
    print("Puedes ingresar a la disco")