
# and --> devuelve verdadero si ambas son verdaderas
# or --> devuelve verdadero si una de las afirmaciones es verdadera
# not devuelve lo opuesto al valor que siga

x = 15
y = 5
booleano= x > 3 and x < 10
booleano_1= x > 3 or x < 10
booleano_2= x > 3 or x != 10
booleano_3= not x == 0


print(booleano)
print(booleano_1)
print(booleano_2)
print(booleano_3)

a = x != y
b = y < x
booleano_4 = not (a and b)

print(booleano_4)