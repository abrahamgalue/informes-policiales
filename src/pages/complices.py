"""Registro de los Complices"""
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class FormularioComplices(tk.Tk):
    """Formulario de registro de los complices"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Complices')
        self.minsize(400, 400)
        self.resizable(0, 0)

        title_label = tk.Label(text='REGISTRO DE LOS COMPLICES')
        title_label.grid(row=0, column=1, pady=10)

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
            width=20,
            values=["M", "F"]
        )
        self.sex_entry.current(0)
        self.sex_entry.grid(row=5, column=1)

        phone_label = tk.Label(text="Número de teléfono:")
        phone_label.grid(row=6, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(width=20)
        self.phone_entry.grid(row=6, column=1)

        address_label = tk.Label(text="Dirección:")
        address_label.grid(row=7, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(width=20)
        self.address_entry.grid(row=7, column=1)

        nationality_label = tk.Label(text="Nacionalidad:")
        nationality_label.grid(row=8, column=0, sticky=tk.W)
        self.nationality_entry = ttk.Combobox(
            state="readonly", width=20
        )
        paises = sorted(['Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Brasil', 'Canadá', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'República Dominicana', 'Ecuador', 'El Salvador', 'Estados Unidos', 'Guatemala', 'Guyana', 'Haití', 'Honduras', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'Saint Kitts y Nevis', 'Santa Lucía', 'San Vicente y las Granadinas', 'Surinam', 'Trinidad y Tobago', 'Uruguay', 'Venezuela']

                        )
        self.nationality_entry['values'] = paises
        self.nationality_entry.current(0)
        self.nationality_entry.grid(row=8, column=1)

        alias_label = tk.Label(text="Alias:")
        alias_label.grid(row=9, column=0, sticky=tk.W)
        self.alias_entry = tk.Entry(width=20)
        self.alias_entry.grid(row=9, column=1)

        btn_guardar = tk.Button(
            text='Guardar', command=self.save_data)
        btn_guardar.grid(row=10, column=2)

        btn_limpiar = tk.Button(
            text='Siguiente', command=self.next_page)
        btn_limpiar.grid(row=10, column=3)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""

        patron_nombre = r'^[\S]{1,45}$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_apellido = r'^[\S]{1,45}$'
        self.regex_apellido = re.compile(patron_apellido)

        patron_fecha = r'^([0-9]{4})-((?:0?[1-9]|1[0-2])|(?:0?[1-9]|1[0-2]|2[0-8]))-((?:0?[1-9]|[1-2][0-9]|3[0-1]))$'
        self.regex_fecha = re.compile(patron_fecha)

        patron_telefono = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){5,6}$"
        self.regex_telefono = re.compile(patron_telefono)

        patron_direccion = r'^.{1,200}$'
        self.regex_direccion = re.compile(patron_direccion)

        patron_nacionalidad = r'^[a-zA-Z0-9_\-.]{0,45}$'
        self.regex_nacionalidad = re.compile(patron_nacionalidad)

        patron_alias = r'^.{0,45}$'
        self.regex_alias = re.compile(patron_alias)

    def save_data(self):
        """Create a dictionary"""

        nombre = self.name_entry.get()

        if re.match(self.regex_nombre, nombre) is None:
            messagebox.showwarning(
                'Nombre inválido', 'El campo Nombre es obligatorio y debe tener máximo 45 caracteres.')
            return

        apellido = self.lastname_entry.get()

        if re.match(self.regex_apellido, apellido) is None:
            messagebox.showwarning(
                'Apellido inválido', 'El campo Apellido es obligatorio y debe tener máximo 45 caracteres.')
            return

        fecha = self.dob_entry.get().strip()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'El campo Fecha de nacimiento debe cumplir con el formato YYYY-MM-DD (e.g., 2004-09-18).')
            return

        telefono = self.phone_entry.get().strip()

        if re.match(self.regex_telefono, telefono) is None:
            messagebox.showwarning(
                'Teléfono inválido', 'El campo Teléfono debe tener máximo 15 caracteres (e.g., +51 987 654 323).')
            return

        direccion = self.address_entry.get().strip()

        if re.match(self.regex_direccion, direccion) is None:
            messagebox.showwarning(
                'Dirección inválida', 'El campo Dirección es obligatorio y debe tener máximo 200 caracteres.')
            return

        alias = self.alias_entry.get().strip()

        if re.match(self.regex_alias, alias) is None:
            messagebox.showwarning(
                'Alias inválido', 'El campo Alias debe tener máximo 45 caracteres.')
            return

        criminal_data = {
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

        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        self.clean()

    def next_page(self):
        """Cambiar a la siguiente página"""
        from pages.condena import FormularioCondena
        self.destroy()
        FormularioCondena()

    def clean(self):
        """Limpiar los campos del formulario"""
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.sex_entry.current(0)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.nationality_entry.current(0)
        self.alias_entry.delete(0, tk.END)


def main():
    """Renderizar la aplicacion"""
    app = FormularioComplices()
    app.mainloop()


if __name__ == '__main__':
    main()
