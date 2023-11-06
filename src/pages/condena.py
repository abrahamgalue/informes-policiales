"""Registro de Condena"""
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import re
from tkinter import *


class FormularioCriminal(tk.Tk):
    """Formulario de registro de criminal"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro de Condena')
        self.minsize(400, 400)

        title_label = tk.Label(text='REGISTRO DE CONDENA')
        title_label.grid(row=0, column=1, pady=10)

        date_label = tk.Label(text="Fecha:")
        date_label.grid(row=1, column=0, sticky=tk.W)
        self.date_entry = tk.Entry(width=20)
        self.date_entry.grid(row=1, column=1)

        judgment_label = tk.Label(text="Sentencia:")
        judgment_label.grid(row=2, column=0, sticky=tk.W)
        self.judgment_entry = tk.Entry(width=20)
        self.judgment_entry.grid(row=2, column=1)

        btn_guardar = tk.Button(
            text='Guardar', command=self.save_data)
        btn_guardar.grid(row=3, column=2)

        btn_limpiar = tk.Button(
            text='Limpiar', command=self.clean)
        btn_limpiar.grid(row=3, column=3)

        btn_salir = tk.Button(text='Salir', command=self.exit)
        btn_salir.grid(row=3, column=4)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""

        patron_fecha = r'^([0-9]{4})-(0[1-9]|1[0-2])-((?:0?[1-9]|[1-2][0-9]|3[0-1]))$'
        self.regex_fecha = re.compile(patron_fecha)

        patron_sentencia = r'^[a-zA-Z0-9_\-.\s]{1,200}$'
        self.regex_sentencia = re.compile(patron_sentencia)

    def save_data(self):
        """Create a dictionary"""

        fecha = self.date_entry.get().strip()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'La fecha no es válida')
            return

        criminal_data = {
            "Fecha": self.date_entry.get(),
            "Sentencia": self.judgment_entry.get()
        }

        print(criminal_data)

        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        self.clean()
        return

    def clean(self):
        """Limpiar los campos del formulario"""
        self.date_entry.delete(0, tk.END)
        self.judgment_entry.delete(0, tk.END)

    def exit(self):
        from registro_criminal import FormularioCriminal
        """Salir de la aplicación"""
        self.destroy()
        FormularioCriminal()


def main():
    """Renderizar la aplicacion"""
    app = FormularioCriminal()
    app.mainloop()


if __name__ == '__main__':
    main()
