"""Registro de Arresto"""
import re
import tkinter as tk
from tkinter import messagebox


class FormularioArresto(tk.Tk):
    """Formulario de registro de arresto"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Arresto')
        self.minsize(400, 400)
        self.resizable(0, 0)

        title_label = tk.Label(text='REGISTRO DE ARRESTO')
        title_label.grid(row=0, column=1, pady=10)

        arrest_date_label = tk.Label(text="Fecha:")
        arrest_date_label.grid(row=1, column=0, sticky=tk.W)
        self.arrest_date_entry = tk.Entry(width=20)
        self.arrest_date_entry.grid(row=1, column=1)

        hour_label = tk.Label(text="Hora:", justify=tk.LEFT)
        hour_label.grid(row=2, column=0, sticky=tk.W)
        self.hour_entry = tk.Entry(width=20)
        self.hour_entry.grid(row=2, column=1)

        place_label = tk.Label(text="Lugar:")
        place_label.grid(row=3, column=0, sticky=tk.W)
        self.place_entry = tk.Entry(width=20)
        self.place_entry.grid(row=3, column=1)

        crime_label = tk.Label(text="Delito:")
        crime_label.grid(row=4, column=0, sticky=tk.W)
        self.crime_entry = tk.Entry(width=20)
        self.crime_entry.grid(row=4, column=1)

        type_of_crime_label = tk.Label(text="Tipo de Delito:")
        type_of_crime_label.grid(row=5, column=0, sticky=tk.W)
        self.type_of_crime_entry = tk.Entry(width=20)
        self.type_of_crime_entry.grid(row=5, column=1)

        description_label = tk.Label(text="Descripción:")
        description_label.grid(row=6, column=0, sticky=tk.W)
        self.description_entry = tk.Entry(width=20)
        self.description_entry.grid(row=6, column=1)

        btn_guardar = tk.Button(
            text='Siguiente', command=self.save_data)
        btn_guardar.grid(row=7, column=2)

        btn_limpiar = tk.Button(
            text='Limpiar', command=self.clean)
        btn_limpiar.grid(row=7, column=3)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""

        patron_fecha = r'^([0-9]{4})-((?:0?[1-9]|1[0-2])|(?:0?[1-9]|1[0-2]|2[0-8]))-((?:0?[1-9]|[1-2][0-9]|3[0-1]))$'
        self.regex_fecha = re.compile(patron_fecha)

        patron_hora = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
        self.regex_hora = re.compile(patron_hora)

        patron_lugar = r'^.{1,60}$'
        self.regex_lugar = re.compile(patron_lugar)

        patron_delito = r'^.{1,45}$'
        self.regex_delito = re.compile(patron_delito)

        patron_tipo_delito = r'^.{1,45}$'
        self.regex_tipo_delito = re.compile(patron_tipo_delito)

        patron_descripcion = r'^.{1,200}$'
        self.regex_descripcion = re.compile(patron_descripcion)

    def save_data(self):
        """Create a dictionary"""

        fecha = self.arrest_date_entry.get()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'El campo Fecha de nacimiento debe cumplir con el formato YYYY-MM-DD (e.g., 1958-08-29).')
            return

        hora = self.hour_entry.get()

        if re.match(self.regex_hora, hora) is None:
            messagebox.showwarning(
                'Hora inválida', 'El campo Hora debe cumplir con el formato HH:MM:SS (e.g., 10:30:12).')
            return

        lugar = self.place_entry.get()

        if re.match(self.regex_lugar, lugar) is None:
            messagebox.showwarning(
                'Lugar inválido', 'El campo Lugar es obligatorio y debe tener máximo 60 caracteres.')
            return

        delito = self.crime_entry.get()

        if re.match(self.regex_delito, delito) is None:
            messagebox.showwarning(
                'Delito inválido', 'El campo delito es obligatorio y debe tener máximo 45 caracteres.')
            return

        tipo_delito = self.type_of_crime_entry.get()

        if re.match(self.regex_tipo_delito, tipo_delito) is None:
            messagebox.showwarning(
                'Tipo de delito inválido', 'El campo tipo de delito es obligatorio y debe tener máximo 45 caracteres.')
            return

        descripcion = self.description_entry.get()

        if re.match(self.regex_descripcion, descripcion) is None:
            messagebox.showwarning(
                'Descripción inválida', 'El campo Descripción es obligatorio y debe tener máximo 200 caracteres.')
            return

        criminal_data = {
            "Fecha": self.arrest_date_entry.get(),
            "Hora": self.hour_entry.get(),
            "Lugar": self.place_entry.get(),
            "Delito": self.crime_entry.get(),
            "Tipo de Delito": self.type_of_crime_entry.get(),
            "Descripción": self.description_entry.get()
        }
        print(criminal_data)

        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        from pages.criminal import FormularioCriminal
        self.destroy()
        FormularioCriminal()

    def clean(self):
        """Limpiar los campos del formulario"""
        self.arrest_date_entry.delete(0, tk.END)
        self.hour_entry.delete(0, tk.END)
        self.place_entry.delete(0, tk.END)
        self.crime_entry.delete(0, tk.END)
        self.type_of_crime_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)


def main():
    """Renderizar la aplicacion"""
    app = FormularioArresto()
    app.mainloop()


if __name__ == '__main__':
    main()
