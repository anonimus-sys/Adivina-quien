from modulos.juego import seleccionar_personaje_secreto, mostrar_personajes
from modulos.cargar_datos import cargar_personajes
from modulos.preguntas import mostrar_menu_preguntas, comprobar_caracteristica
from modulos.archivos import guardar_resultado
### comentario
def main():
    print("=======================================")
    print("   ¡BIENVENIDO A ADIVINA QUIÉN!        ")
    print("=======================================")
    
    nombre_jugador = input("Introduce tu nombre para empezar: ")
    
    ruta_archivo = "data/personajes.txt"
    lista_personajes = cargar_personajes(ruta_archivo)
    
    mostrar_personajes(lista_personajes)
    secreto = seleccionar_personaje_secreto(lista_personajes)
    
    # [DEBUG] Borra esta línea cuando lo entregues
    print(f"--- [DEBUG] El personaje secreto es: {secreto['nombre']} ---")
    
    # 2. Creamos el contador de preguntas
    contador_preguntas = 0
    
    jugando = True
    while jugando:
        mostrar_menu_preguntas()
        opcion = input("\nSelecciona una opción (1-9): ")
        
        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            # Sumamos una pregunta al contador
            contador_preguntas += 1
            respuesta = comprobar_caracteristica(opcion, secreto)
            print(f"\nRespuesta del sistema: {respuesta}")
            
        elif opcion == "8":
            intento = input("\n¿Quién crees que es el personaje secreto?: ").strip()
            
            if intento.lower() == secreto["nombre"].lower():
                print(f"\n¡FELICITACIONES! ¡GANASTE! El personaje era {secreto['nombre']}.")
                resultado = "ganó"
            else:
                print(f"\nLo siento, te equivocaste. El personaje secreto era {secreto['nombre']}. ¡Perdiste!")
                resultado = "perdió"
            
            # 3. Guardamos el resultado automáticamente en el archivo antes de salir
            guardar_resultado(nombre_jugador, resultado, secreto["nombre"], contador_preguntas)
            print("Partida guardada en el historial.")
            
            jugando = False 
            
        elif opcion == "9":
            print("\nGracias por jugar. ¡Hasta la próxima!")
            jugando = False
            
        else:
            print("\nOpción inválida. Por favor, digita un número del 1 al 9.")

if __name__ == "__main__":
    main()