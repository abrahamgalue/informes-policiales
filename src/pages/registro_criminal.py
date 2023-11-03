"""Registro del Criminal"""
import re
import tkinter as tk
from tkinter import ttk


class FormularioCriminal(tk.Tk):
    """Formulario de registro de criminal"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Criminal')
        self.minsize(400, 400)

        title_label = tk.Label(text='REGISTRO DEL CRIMINAL')
        title_label.grid(row=0, column=1, pady=10)

        dni_label = tk.Label(text="Documento Identidad:", justify=tk.LEFT)
        validador = (self.register(self.validar), '%i', '%P')
        dni_label.grid(row=1, column=0, sticky=tk.W)
        self.dni_entry = tk.Entry(self, validate='key', width=20,
                                  validatecommand=validador, invalidcommand=self.invalidar)
        self.dni_entry.grid(row=1, column=1)

        name_label = tk.Label(text="Nombre:", justify=tk.LEFT)
        name_label.grid(row=2, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(width=20)
        self.name_entry.grid(row=2, column=1)

        dob_label = tk.Label(text="Fecha de nacimiento:")
        dob_label.grid(row=3, column=0, sticky=tk.W)
        self.dob_entry = tk.Entry(width=20)
        self.dob_entry.grid(row=3, column=1)

        sex_label = tk.Label(text="Sexo:")
        sex_label.grid(row=4, column=0, sticky=tk.W)

        self.sex_entry = ttk.Combobox(
            state="readonly",
            width=20,
            values=["M", "F"]
        )
        self.sex_entry.current(0)
        self.sex_entry.grid(row=4, column=1)

        phone_label = tk.Label(text="Número de teléfono:")
        phone_label.grid(row=5, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(width=20)
        self.phone_entry.grid(row=5, column=1)

        address_label = tk.Label(text="Dirección:")
        address_label.grid(row=6, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(width=20)
        self.address_entry.grid(row=6, column=1)

        civil_status_label = tk.Label(text="Estado civil:")
        civil_status_label.grid(row=7, column=0, sticky=tk.W)

        self.civil_status_entry = ttk.Combobox(
            state="readonly",
            width=20,
            values=["Soltero", "Casado"]
        )
        self.civil_status_entry.current(0)
        self.civil_status_entry.grid(row=7, column=1)

        nationality_label = tk.Label(text="Nacionalidad:")
        nationality_label.grid(row=8, column=0, sticky=tk.W)
        self.nationality_entry = ttk.Combobox(
            state="readonly", width=20
        )
        paises = sorted(['Colombia', 'Chile', 'Venezuela',
                        'México', 'Brasil', 'Uruguay'])
        self.nationality_entry['values'] = paises
        self.nationality_entry.current(0)
        self.nationality_entry.grid(row=8, column=1)

        alias_label = tk.Label(text="Alias:")
        alias_label.grid(row=9, column=0, sticky=tk.W)
        self.alias_entry = tk.Entry(width=20)
        self.alias_entry.grid(row=9, column=1)

        btn_guardar = tk.Button(
            text='Guardar', command=self.save_data, state='disabled')
        btn_guardar.grid(row=10, column=2)

        btn_limpiar = tk.Button(
            text='Limpiar', command=self.clean)
        btn_limpiar.grid(row=10, column=3)

        btn_salir = tk.Button(text='Salir', command=self.exit)
        btn_salir.grid(row=10, column=4)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""
        patron_documento = r'^[0-9]{7,10}$'
        self.regex_documento = re.compile(patron_documento)

        patron_nombre = r'^[a-zA-Z0-9_\-.]{0,60}$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_fecha = r'^\d{4}-\d{2}-\d{2}$'
        self.regex_fecha = re.compile(patron_fecha)

        patron_telefono = r'^\d{7,10}$'
        self.regex_telefono = re.compile(patron_telefono)

        patron_direccion = r'^[a-zA-Z0-9_\-.]{0,200}$'
        self.regex_direccion = re.compile(patron_direccion)

        patron_nacionalidad = r'^[a-zA-Z0-9_\-.]{0,45}$'
        self.regex_nacionalidad = re.compile(patron_nacionalidad)

        patron_alias = r'^[a-zA-Z0-9_\-.]{0,45}$'
        self.regex_alias = re.compile(patron_alias)

    # def on_validate(self, indice, usuario):
    #     return self.regex_documento.match()

    def save_data(self):
        """Create a dictionary"""

        criminal_data = {
            "Nombre": self.name_entry.get(),
            "Fecha de nacimiento": self.dob_entry.get(),
            "Sexo": self.sex_entry.get(),
            "Número de teléfono": self.phone_entry.get(),
            "Dirección": self.address_entry.get(),
            "Estado civil": self.civil_status_entry.get(),
            "Nacionalidad": self.nationality_entry.get(),
            "Alias": self.alias_entry.get()
        }
        print(criminal_data)

    def clean(self):
        """Limpiar los campos del formulario"""
        self.dni_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.sex_entry.current(0)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.civil_status_entry.current(0)
        self.nationality_entry.current(0)
        self.alias_entry.delete(0, tk.END)

    def exit(self):
        """Salir de la aplicación"""
        self.destroy()


def main():
    """Renderizar la aplicacion"""
    app = FormularioCriminal()
    app.mainloop()


if __name__ == '__main__':
    main()
