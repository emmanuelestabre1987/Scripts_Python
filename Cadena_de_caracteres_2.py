a= "Hola"
b="Mundo"

c=a+" "+b

print(c)
txt= " El contenido del curso va a durar: "
horas=10

# concatenado=txt+horas --> Esto no funcionaria

concatenado=txt+str(horas) # Esto si

print(concatenado)

# Otra forma es esta

horas_2=15
txt_2= "El nuevo curso va a durar: {} horas "
print(txt_2.format(horas_2))



horas_3= 20
clases= 60
txt_3= "El contenido de este curso va a durar {1} horas y tendra {0} clases" # Con el numero aca los puedo ordenar
print(txt_3.format(clases, horas_3))

txt_4= ' La mejor serie que vi en mi vida es "Vikingos"' # Puedo usar comillas simple afuera y comillas doble adentro

txt_5= " La mejor serie que vi en mi vida es \"Vikingos\"" # Puedo hacer un escape de caracteres con las barras diagonales \

print(txt_4)
print(txt_5)

# /n nos sirve para hacer saltos de linea en strings con double o single quote

txt_6= ' Aguante boquita:\ncarajo'

print(txt_6)


