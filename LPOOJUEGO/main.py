from jugador import Jugador
from juego import JuegoAdivinanza

nombre1 = input("Ingrese el nombre del Jugador 1: ")
nombre2 = input("Ingrese el nombre del Jugador 2: ")

jugador1 = Jugador(nombre1)
jugador2 = Jugador(nombre2)

juego = JuegoAdivinanza(jugador1, jugador2)
juego.iniciar_juego()
