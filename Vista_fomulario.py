
class Vista_formulario:
    def __init__(self):
        self.titulo = "--- Programa de números ---"
        self.pregunta_campo_numero = "Digite un número entero: "

    def pedir_numero(self) -> int:
        print(self.titulo)
        while True:
            try:
                valor = int(input(self.pregunta_campo_numero))
                return valor
            except ValueError:
                print("Por favor ingrese solo números enteros.")

    def imprimir_mensaje(self, dato_mensaje: str):
        print(f"INFO: {dato_mensaje}")

    def imprimir_resultado(self, numero: int, paridad: str, naturaleza: str):
        print("\n" + "="*30)
        print(f"El número {numero} es:{paridad} y {naturaleza}")
        print("="*30 + "\n")