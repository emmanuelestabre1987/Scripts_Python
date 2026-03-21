familia={
    "padre":{
        "Nombre":"Raul",
        "profesion":"carpintero"
    },
    "madre":{
        "nombre":"patricia",
        "profesion":"abogada"
    },
    "hijo":{
        "nombre":"pedro",
        "profesion":"desempleado"
    }
}

print(familia["padre"],["profesion"])

for pariente, data in familia.items():
    print(pariente)

    for clave in data:
        print(clave + ":",data[clave])