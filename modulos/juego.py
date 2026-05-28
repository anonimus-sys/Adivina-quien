import random

def seleccionar_personaje_secreto(lista_personajes):
    """
    Toma la lista de personajes y elige uno al azar.
    Retorna el diccionario del personaje secreto.
    """
    # random.choice elige un elemento aleatorio de una lista
    personaje_secreto = random.choice(lista_personajes)
    return personaje_secreto


def mostrar_personajes(lista_personajes):
    """
    Muestra en la consola la lista de todos los personajes 
    que siguen en juego con sus características.
    """
    print("\n=== PERSONAJES DISPONIBLES ===")
    for p in lista_personajes:
        # Formateamos bonito para que el usuario lo lea fácil en la consola
        print(f"- {p['nombre']} (Género: {p['genero']}, Cabello: {p['cabello']}, Gafas: {p['gafas']}, Sombrero: {p['sombrero']}, Barba: {p['barba']}, Ojos: {p['ojos']})")
    print("===============================\n")