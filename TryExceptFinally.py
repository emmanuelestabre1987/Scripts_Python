# Estructura de control: Manejo de errores
#try, except, finally

# Manejo de division por cero (No permitida)

'''a = 10
b = 0 
c= a/b

print(c)'''

'''a = 10
b = 0 
try:
    resultado=a/b
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Hola mi nombre es Emmanuel y este mensaje quiero que salga a pesar de los errores")'''


a = 10
b = 0 
resultado= 0
try: # intenta hacer algo
    resultado=a/b
    print(resultado)
except ZeroDivisionError: # Si tiene error lo maneja
    print("No se puede dividir por cero")
finally: # Se ejecuta siempre
    resultado= 0

print(resultado)