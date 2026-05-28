def cargar_personajes(ruta):
    lista_personajes = []
    with open(ruta, "r", encoding = "utf-8") as personajes:
        guardar = personajes.readline()
        llaves = guardar.split(",")
        print(llaves)
        for personaje in personajes:
            persona_limpio = personaje.strip().split(",")
        diccionario_personaje = {}
        for i in range(len(llaves)):
            llave = llaves[i]
            valor = persona_limpio[i]
            diccionario_personaje[llave] = valor
        lista_personajes.append(diccionario_personaje)
    return lista_personajes