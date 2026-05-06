from Numero_modelo import Numero
from Vista_fomulario import Vista_formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Vista_formulario()

    def tomar_numero(self):
        valor = self.obj_vista.pedir_numero()
        self.obj_numero.set_numero(valor)
        self.obj_vista.imprimir_mensaje("Número recibido.")

    def procesar(self):
        numero_actual = self.obj_numero.get_numero()
        paridad = self.obj_numero.validar_paridad()
        naturaleza = self.obj_numero.validar_naturaleza()
        self.obj_vista.imprimir_resultado(numero_actual, paridad, naturaleza)