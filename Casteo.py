
# Texto(str)
variable1="Texto"
variable2="123456"
variable3="texto123"

# Numericas (int, float, complex)

variable4=10
variable5= 2.5
variable6= 1j

# Casteo de str a int
variableCasteada=int(variable2)

# Casteo de int a str
variableCasteada2=str(variable4)

print(type(variable1))#<class 'str'>
print(type(variableCasteada))#<class 'str'> - Casteo la variable
print(type(variable3))#<class 'str'>
print(type(variable4))#<class 'int'>
print(type(variable5))#<class 'float'>
print(type(variable6))#<class 'complex'>

print(type(variableCasteada))
print(type(variableCasteada2))

# Casteo de listas

lista=["manzana","pera","naranja"]
x= list(("manzana","pera","naranja"))


print(type(x))

# Castear tupla a lista
tupla=("manzana","pera","naranja")
list1 = list(tupla)

print(type(list1))

print(tupla)
