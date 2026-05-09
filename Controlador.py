from Numero_modelo import Numero
from Vista_fomulario import Vista_formulario

class Controlador:
    def __init__(self):
        self.obj_numero = Numero()
        self.obj_vista = Vista_formulario(self)

    def tomar_numero(self):
        try:
            valor = self.obj_vista.pedir_numero()
            self.obj_numero.set_numero(valor)
            self.obj_vista.imprimir_mensaje("Numero recibido correctamente.")
            self.imprimir_numero()
            
        except ValueError:
            self.obj_vista.imprimir_mensaje("Error: Debe ingresar un número válido.")

    def imprimir_numero(self):
        num = self.obj_numero.get_numero()
        resultado = self.obj_numero.validar_numero(num)
        self.obj_vista.imprimir_numero(resultado)

    def iniciar_app(self):
        self.obj_vista.iniciar()
