#----------------------------------
# CONJUNTO (SET) [[Coleccion no ordenada y mutable de elementos unicos]]
#----------------------------------

conjunto_frutas={"Manzana","Platano","Pera"}

print(conjunto_frutas)

# No tiene un orden definido 
# No permite duplicados
# El booleano True es el numero 1 para python
# El booleano False es el numero 0 para python
# Es decir 0 y 1 no pueden ir con True y False

longitud= len(conjunto_frutas)

print(longitud)

conjunto_frutas3= set(( "Manzana","pera","Uva"))

print(conjunto_frutas3)

manzana=set(("Manzana")) # Este caso es como un contador unico de los elementos

print(manzana) 