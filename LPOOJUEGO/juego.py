from jugador import Jugador

class JuegoAdivinanza:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def iniciar_juego(self):
        print(f"{self.jugador1.obtener_nombre()} y {self.jugador2.obtener_nombre()}, elijan su número secreto de 4 dígitos.")
        self.jugador1.establecer_numero_secreto()
        self.jugador2.establecer_numero_secreto()
        
        turno = 0
        ganador = None
        while not ganador:
            jugador_actual = self.jugador1 if turno % 2 == 0 else self.jugador2
            oponente = self.jugador2 if turno % 2 == 0 else self.jugador1
            
            print(f"\nTurno de {jugador_actual.obtener_nombre()}")
            print("Historial de intentos:", jugador_actual.obtener_historial())
            intento = input("Ingresa tu intento de 4 dígitos: ")
            
            try:
                coincidencias = oponente.adivinar(intento)
                print(f"Coincidencias en posición correcta: {coincidencias}")
                
                if coincidencias == 4:
                    if not ganador:
                        ganador = jugador_actual
                        print(f"{jugador_actual.obtener_nombre()} ha adivinado el número de {oponente.obtener_nombre()}!")
                        if turno % 2 == 0:  # Si es el turno del jugador 1, jugador 2 tiene una oportunidad
                            print(f"{oponente.obtener_nombre()} tienes una oportunidad de empatar.")
                        else:
                            break
                    else:
                        print(f"{jugador_actual.obtener_nombre()} has empatado el juego")
                        break
            except ValueError as e:
                print("error", e)
                continue
            
            turno += 1
        
        print(f"El juego ha terminado. ¡Felicitaciones {ganador.obtener_nombre()}!")


