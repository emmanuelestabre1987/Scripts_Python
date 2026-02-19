
a = "En este texto pondremos algunas tecnologias = Python, R, Django, y Tensorflow"

print("Django" in a)
print("Django" not in a)

# Como solucionar los keysensitive

textominuscula = a.lower()
abuscar= "TENSORFLOW".lower()
abuscar= "       TENSORFLOW      ".strip().lower() # Strip quita los espacios
print(abuscar in textominuscula )