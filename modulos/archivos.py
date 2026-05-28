def guardar_resultado(jugador, resultado, personaje, preguntas):
    """
    Guarda una línea en el archivo data/historial.txt con el resumen de la partida.
    """
    ruta = "data/historial.txt"
    
    # Abrimos en modo "a" (append) para añadir texto al final sin borrar lo anterior
    with open(ruta, "a", encoding="utf-8") as archivo:
        linea = f"Jugador: {jugador} | Resultado: {resultado} | Personaje: {personaje} | Preguntas usadas: {preguntas}\n"
        archivo.write(linea)