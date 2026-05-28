def mostrar_menu_preguntas():
    """
    Muestra las opciones de preguntas disponibles para el usuario.
    """
    print("\n¿Qué quieres preguntar o hacer?")
    print("1. ¿Es de género femenino?")
    print("2. ¿Es de género masculino?")
    print("3. ¿Tiene gafas?")
    print("4. ¿Tiene sombrero?")
    print("5. ¿Tiene barba?")
    print("6. ¿Tiene el cabello negro?")
    print("7. ¿Tiene el cabello castaño?")
    print("8. Intentar adivinar el personaje")
    print("9. Salir del juego")


def comprobar_caracteristica(opcion, personaje_secreto):
    """
    Compara la opción elegida con el personaje secreto.
    Retorna un mensaje con el "SÍ" o "NO" y la característica evaluada.
    """
    # Dependiendo del número que elija el usuario, revisamos una llave y un valor en el diccionario
    if opcion == "1":
        cumple = (personaje_secreto["genero"] == "femenino")
    elif opcion == "2":
        cumple = (personaje_secreto["genero"] == "masculino")
    elif opcion == "3":
        cumple = (personaje_secreto["gafas"] == "si")
    elif opcion == "4":
        cumple = (personaje_secreto["sombrero"] == "si")
    elif opcion == "5":
        cumple = (personaje_secreto["barba"] == "si")
    elif opcion == "6":
        cumple = (personaje_secreto["cabello"] == "negro")
    elif opcion == "7":
        cumple = (personaje_secreto["castano"] == "si" or personaje_secreto["cabello"] == "castano")
    else:
        return None  # Para opciones que no son preguntas directas (adivinar o salir)

    # Retornamos la respuesta formal del juego
    if cumple:
        return "¡SÍ lo tiene / SÍ lo es!"
    else:
        return "NO lo tiene / NO lo es."