
class Numero:
    def __init__(self):
        self.dato_numero = 0

    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def get_numero(self):
        return self.dato_numero

    def validar_paridad(self):
        if self.dato_numero % 2 == 0:
            return "Par"
        return "Impar"

    def validar_naturaleza(self):
        if self.dato_numero > 0:
            return "Positivo"
        elif self.dato_numero < 0:
            return "Negativo"
        else:
            return "Neutro"