class Numero:
    def __init__(self):
        self.dato_numero = 0

    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def get_numero(self):
        return self.dato_numero

    def validar_numero(self, dato_numero):
        paridad = "Par" if dato_numero % 2 == 0 else "Impar"
        if dato_numero > 0: nat = "Positivo"
        elif dato_numero < 0: nat = "Negativo"
        else: nat = "Neutro"
        return f"{paridad} y {nat}"
