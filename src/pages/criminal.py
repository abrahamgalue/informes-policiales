"""Registro del Criminal"""
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos = []

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
        self.resizable(0, 0)

        title_label = tk.Label(text='REGISTRO DEL CRIMINAL')
        title_label.grid(row=0, column=1, pady=10)

        dni_label = tk.Label(text="Documento Identidad:", justify=tk.LEFT)
        dni_label.grid(row=1, column=0, sticky=tk.W)
        self.dni_entry = tk.Entry(width=20)
        self.dni_entry.grid(row=1, column=1)

        name_label = tk.Label(text="Nombre:", justify=tk.LEFT)
        name_label.grid(row=2, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(width=20)
        self.name_entry.grid(row=2, column=1)

        lastname_label = tk.Label(text="Apellido:", justify=tk.LEFT)
        lastname_label.grid(row=3, column=0, sticky=tk.W)
        self.lastname_entry = tk.Entry(width=20)
        self.lastname_entry.grid(row=3, column=1)

        dob_label = tk.Label(text="Fecha de nacimiento:")
        dob_label.grid(row=4, column=0, sticky=tk.W)
        self.dob_entry = tk.Entry(width=20)
        self.dob_entry.grid(row=4, column=1)

        sex_label = tk.Label(text="Sexo:")
        sex_label.grid(row=5, column=0, sticky=tk.W)

        self.sex_entry = ttk.Combobox(
            state="readonly",
            values=["Masculino", "Femenino"]
        )
        self.sex_entry.current(0)
        # self.sex_entry.grid(row=5, column=1)
        self.sex_entry.place(
            relheight=0.056, relwidth=0.307, relx=0.33, rely=0.312)

        phone_label = tk.Label(text="Número de teléfono:")
        phone_label.grid(row=6, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(width=20)
        self.phone_entry.grid(row=6, column=1)

        address_label = tk.Label(text="Dirección:")
        address_label.grid(row=7, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(width=20)
        self.address_entry.grid(row=7, column=1)

        nationality_label = tk.Label(text="Nacionalidad:")
        nationality_label.grid(row=9, column=0, sticky=tk.W)
        self.nationality_entry = ttk.Combobox(
            state="readonly", width=20
        )
        paises = sorted(['Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Brasil', 'Canadá', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'República Dominicana', 'Ecuador', 'El Salvador', 'Estados Unidos', 'Guatemala', 'Guyana', 'Haití', 'Honduras', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'Saint Kitts y Nevis', 'Santa Lucía', 'San Vicente y las Granadinas', 'Surinam', 'Trinidad y Tobago', 'Uruguay', 'Venezuela']

                        )
        self.nationality_entry['values'] = paises
        self.nationality_entry.current(0)
        self.nationality_entry.grid(row=9, column=1)

        alias_label = tk.Label(text="Alias:")
        alias_label.grid(row=10, column=0, sticky=tk.W)
        self.alias_entry = tk.Entry(width=20)
        self.alias_entry.grid(row=10, column=1)

        btn_guardar = tk.Button(
            text='Guardar', command=self.save_data)
        btn_guardar.grid(row=11, column=2)

        btn_limpiar = tk.Button(
            text='Limpiar', command=self.clean)
        btn_limpiar.grid(row=11, column=3)

        btn_salir = tk.Button(text='Salir', command=self.exit)
        btn_salir.grid(row=11, column=4)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""
        patron_documento = r'^[0-9]{7,10}$'
        self.regex_documento = re.compile(patron_documento)

        patron_nombre = r'^[\S]{1,45}$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_apellido = r'^[\S]{1,45}$'
        self.regex_apellido = re.compile(patron_apellido)

        patron_fecha = r'^([0-9]{4})-(0[1-9]|1[0-2])-((?:0?[1-9]|[1-2][0-9]|3[0-1]))$'
        self.regex_fecha = re.compile(patron_fecha)

        patron_telefono = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){5,6}$"
        self.regex_telefono = re.compile(patron_telefono)

        patron_direccion = r'^.{1,200}$'
        self.regex_direccion = re.compile(patron_direccion)

        patron_alias = r'^.{0,45}$'
        self.regex_alias = re.compile(patron_alias)

    def save_data(self):
        """Create a dictionary"""

        documento = self.dni_entry.get().strip()

        if re.match(self.regex_documento, documento) is None:
            messagebox.showwarning(
                'Documento inválido', 'El documento no es válido')
            return

        nombre = self.name_entry.get()

        if re.match(self.regex_nombre, nombre) is None:
            messagebox.showwarning(
                'Nombre inválido', 'El nombre no es válido')
            return

        apellido = self.lastname_entry.get()

        if re.match(self.regex_apellido, apellido) is None:
            messagebox.showwarning(
                'Apellido inválido', 'El apellido no es válido')
            return

        fecha = self.dob_entry.get().strip()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'La fecha no es válida')
            return

        telefono = self.phone_entry.get().strip()

        if re.match(self.regex_telefono, telefono) is None:
            messagebox.showwarning(
                'Teléfono inválido', 'El teléfono no es válido')
            return

        direccion = self.address_entry.get().strip()

        if re.match(self.regex_direccion, direccion) is None:
            messagebox.showwarning(
                'Dirección inválida', 'La dirección no es válida')
            return

        alias = self.alias_entry.get().strip()

        if re.match(self.regex_alias, alias) is None:
            messagebox.showwarning(
                'Alias inválido', 'El alias no es válido')
            return

        criminal_data = {
            "Documento Identidad": self.dni_entry.get(),
            "Nombre": self.name_entry.get(),
            "Apellido": self.lastname_entry.get(),
            "Fecha de nacimiento": self.dob_entry.get(),
            "Sexo": self.sex_entry.get(),
            "Número de teléfono": self.phone_entry.get(),
            "Dirección": self.address_entry.get(),
            "Nacionalidad": self.nationality_entry.get(),
            "Alias": self.alias_entry.get()
        }
        print(criminal_data)
        datos = list(criminal_data.values())
        from util.implicado import add_persona
        add_persona(datos)

        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        self.clean()
        return

    def clean(self):
        """Limpiar los campos del formulario"""
        from condena import FormularioCondena
        self.dni_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.sex_entry.current(0)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.nationality_entry.current(0)
        self.alias_entry.delete(0, tk.END)
        self.destroy()
        FormularioCondena()

    def exit(self):
        """Salir de la aplicación"""
        self.destroy()


def main():
    """Renderizar la aplicacion"""
    app = FormularioCriminal()
    app.mainloop()


if __name__ == '__main__':
    main()
