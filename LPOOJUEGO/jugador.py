class Jugador:
    def __init__(self, nombre): 
        self.__nombre = nombre
        self.__numero_secreto = None
        self.__historial_intentos = []

    def establecer_numero_secreto(self):
        while True:
            numero = input(f"{self.__nombre}, ingresa tu número secreto (4 dígitos): ")
            if numero.isdigit() and len(numero) == 4:
                self.__numero_secreto = numero
                break
            else:
                print("Error: El número debe tener exactamente 4 dígitos y ser numérico.")
    
    def adivinar(self, intento):
        if not intento.isdigit() or len(intento) != 4:
            raise ValueError("El intento debe ser un número de 4 dígitos.")
        self.__historial_intentos.append(intento)
        return self.__comparar_numeros(intento)
    
    def obtener_historial(self):
        return self.__historial_intentos
    
    def obtener_nombre(self):
        return self.__nombre
    
    def __comparar_numeros(self, intento):
        coincidencias = sum(1 for i in range(4) if intento[i] == self.__numero_secreto[i])
        return coincidencias
