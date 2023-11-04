"""Registro de Señas de Identificación"""
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class FormularioCriminal(tk.Tk):
    """Formulario de señas de identificacion"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Criminal')
        self.minsize(400, 400)

        title_label = tk.Label(text='REGISTRO DE SEÑAS DE IDENTIFICACION')
        title_label.grid(row=0, column=1, pady=10)

        weight_label = tk.Label(text="Peso:")
        weight_label.grid(row=1, column=0, sticky=tk.W)
        self.weight_entry = tk.Entry(width=20)
        self.weight_entry.grid(row=1, column=1)

        height_label = tk.Label(text="Altura:", justify=tk.LEFT)
        height_label.grid(row=2, column=0, sticky=tk.W)
        self.height_entry = tk.Entry(width=20)
        self.height_entry.grid(row=2, column=1)

        skin_color_label = tk.Label(text="Color de piel:", justify=tk.LEFT)
        skin_color_label.grid(row=3, column=0, sticky=tk.W)
        self.skin_color_entry = tk.Entry(width=20)
        self.skin_color_entry.grid(row=3, column=1)

        hair_label = tk.Label(text="Cabello:")
        hair_label.grid(row=4, column=0, sticky=tk.W)
        self.hair_entry = tk.Entry(width=20)
        self.hair_entry.grid(row=4, column=1)

        hair_color_label = tk.Label(text="Color de Cabello:")
        hair_color_label.grid(row=5, column=0, sticky=tk.W)
        self.hair_color_entry = tk.Entry(width=20)
        self.hair_color_entry.grid(row=5, column=1)

        eyes_label = tk.Label(text="Ojos:")
        eyes_label.grid(row=6, column=0, sticky=tk.W)
        self.eyes_entry = tk.Entry(width=20)
        self.eyes_entry.grid(row=6, column=1)

        other_features_label = tk.Label(text="Otras Características:")
        other_features_label.grid(row=7, column=0, sticky=tk.W)
        self.other_features_entry = tk.Entry(width=20)
        self.other_features_entry.grid(row=7, column=1)

        btn_guardar = tk.Button(
            text='Guardar', command=self.save_data)
        btn_guardar.grid(row=8, column=2)

        btn_limpiar = tk.Button(
            text='Limpiar', command=self.clean)
        btn_limpiar.grid(row=8, column=3)

        btn_salir = tk.Button(text='Salir', command=self.exit)
        btn_salir.grid(row=8, column=4)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""
        patron_peso = r'^[0-9]{3}\.[0-9]{2}$'
        self.regex_peso = re.compile(patron_peso)

        patron_altura = r'^[0-9]{3}\.[0-9]{2}$'
        self.regex_altura = re.compile(patron_altura)

        patron_color_piel = r'^[a-zA-Z0-9_\-.\s]{3,45}$'
        self.regex_color_piel = re.compile(patron_color_piel)

        patron_cabello = r'^[a-zA-Z0-9_\-.\s]{4,45}$'
        self.regex_cabello = re.compile(patron_cabello)

        patron_color_cabello = r'^[a-zA-Z0-9_\-.\s]{5,45}$'
        self.regex_color_cabello = re.compile(patron_color_cabello)

        patron_ojos = r'^[a-zA-Z0-9_\-.\s]{0,45}$'
        self.regex_ojos = re.compile(patron_ojos)

        patron_otras_caracteristicas = r'^[a-zA-Z0-9_\-.\s]{0,60}$'
        self.regex_otras_caracteristicas = re.compile(
            patron_otras_caracteristicas)

    def save_data(self):
        """Create a dictionary"""

        peso = self.weight_entry.get().strip()

        if re.match(self.regex_peso, peso) is None:
            messagebox.showwarning(
                'Peso inválido', 'El peso no es válido')
            return

        altura = self.height_entry.get().strip()

        if re.match(self.regex_altura, altura) is None:
            messagebox.showwarning(
                'Altura inválida', 'La altura no es válida')
            return

        color_piel = self.skin_color_entry.get().strip()

        if re.match(self.regex_color_piel, color_piel) is None:
            messagebox.showwarning(
                'Color de piel inválido', 'El color de piel no es válido')
            return

        cabello = self.hair_entry.get().strip()

        if re.match(self.regex_cabello, cabello) is None:
            messagebox.showwarning(
                'Cabello inválido', 'El cabello no es válido')
            return

        color_cabello = self.hair_color_entry.get().strip()

        if re.match(self.regex_color_cabello, color_cabello) is None:
            messagebox.showwarning(
                'Color de cabello inválido', 'El color de cabello no es válido')
            return

        ojos = self.eyes_entry.get().strip()

        if re.match(self.regex_ojos, ojos) is None:
            messagebox.showwarning(
                'Ojos inválidos', 'Los ojos no son válidos')
            return

        otras_caracteristicas = self.other_features_entry.get().strip()

        if re.match(self.regex_otras_caracteristicas, otras_caracteristicas) is None:
            messagebox.showwarning(
                'Otras caracteristicas inválidas', 'Las otras caracteristicas no son válidas')
            return

        criminal_data = {
            "Peso": self.weight_entry.get(),
            "Altura": self.height_entry.get(),
            "Color de Piel": self.skin_color_entry.get(),
            "Cabello": self.hair_entry.get(),
            "Color de Cabello": self.hair_color_entry.get(),
            "Ojos": self.eyes_entry.get(),
            "Otras caracteristicas": self.other_features_entry.get()
        }

        print(criminal_data)

        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        self.clean()
        return

    def clean(self):
        """Limpiar los campos del formulario"""
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.skin_color_entry.delete(0, tk.END)
        self.hair_entry.delete(0, tk.END)
        self.hair_color_entry.delete(0, tk.END)
        self.eyes_entry.delete(0, tk.END)
        self.other_features_entry.delete(0, tk.END)

    def exit(self):
        """Salir de la aplicación"""
        self.destroy()


def main():
    """Renderizar la aplicacion"""
    app = FormularioCriminal()
    app.mainloop()


if __name__ == '__main__':
    main()
