import tkinter as tk
from tkinter import messagebox

class Vista_formulario:
    def __init__(self, controlador):
        self.titulo = "Programa de Números"
        self.pregunta_campo_numero = "Ingrese un número entero:"
        self.campo_dato_numero = None
        self.root = tk.Tk()
        self.root.title(self.titulo)
        self.root.geometry("300x200")
        tk.Label(self.root, text=self.pregunta_campo_numero).pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        tk.Button(self.root, text="Enviar", command=controlador.tomar_numero).pack(pady=20)

    def pedir_numero(self):
        return int(self.entry.get())
    
    def imprimir_mensaje(self, dato_mensaje):
        messagebox.showinfo("Mensaje", dato_mensaje)

    def imprimir_numero(self, dato_numero):
        messagebox.showinfo("Resultado", f"Análisis: {dato_numero}")

    def iniciar(self):
        self.root.mainloop()
