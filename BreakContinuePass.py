# BREAK

'''contador = 0

while contador < 10:
    print(contador)
    if contador == 5:
        break
    contador += 1'''


'''contador = 10
prohibido = 23

while contador < 25:
    print(contador)
    if contador == prohibido:
        break
    contador += 1'''


'''contador = 0


while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
        continue    

print(contador) '''

'''while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
        continue 
    print("imprimir por cada vuelta")   

print(contador) '''

# La palabra continue tiene mas sentido en un for

for i in range(10):
    if i % 2 == 1: # puedo ver numeros pares, si el resto cero ver numeros impares
        continue
    print(i)

# PASS

edad = 17

if edad > 18:
    print("Puedes ingresar a esta institutcion")
elif edad == 18:
    pass # Con el pass no hace nada si el dato no coincide con parametros del condicional.
else:
    print ("No tienes edad suficiente para entrar aqui")