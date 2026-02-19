texto = "hola mundo"
texto2="HoLa MuNdO" 
texto_con_espacios="     Texto con espacios     "
texto_separado="Python,Javascript,Django,React"
lista=["Hola","Juan","Carlos"]
numeros="123456"
letras="abc"
repeticion= "manzana, limon, manzana, pera, anana"

print("capitalize:", texto.capitalize()) # pone la primera letra en mayuscula, resto en minuscula
print("upper:" ,texto.upper()) # convierte el texto entero en mayusculas
print("lower:", texto2.lower()) # Convierte el texto entero en minusculas
print("strip:",texto_con_espacios.strip()) # Elimina el texto con espacios al comienzo y al final
print("replace:", texto_con_espacios.replace("espacios", "bosta")) # Reemplaza una palabra por otra
print("split:", texto_separado.split(",")) # Separa el texto en una lista donde encuentra el caracter especificado
print("join","," .join(lista))# Une los elementos de una lista en un solo texto, usando como separador el texto especificado
print("find", texto2.find("MuNdO")) # Muestra la posicion donde comienza el texto ingresado
print("index", texto2.index("MuNdO")) # Muestra la posicion donde arranca el texto ingresado
print("rfind", repeticion.rfind("manzana")) # Muestra la posicion donde comienza el ultimo texto ingresado
print("Startswith:", texto.startswith("hola"))# Devuelve True si el texto comienza con el texto ingresado
print("endswith:", texto.endswith("mundo"))# Devuelve True si el texto termina con el texto ingresado
print("isdigit:", numeros.isdigit()) # Indica si todos los caracteres son numeros o no. false si hay espacios
print("isalpha:", texto.isalpha()) # Indica si todos los caracteres son letras o no. false si hay espacios
print("isalnum:", letras.isalnum()) # Indica si todos los caracteres son alfanumericos. false si hay espacios
print("isspace", texto.isspace()) # Indica si el string solo esta hecho de espacios.
print("count:", repeticion.count("manzana")) # indica cuantas veces se repite la palabra ingresada.)


