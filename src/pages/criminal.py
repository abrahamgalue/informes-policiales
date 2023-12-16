"""Registro del Criminal"""
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pages.util.persona import get_persona

img = None
ButtonImg = None
ButtonImg2 = None
icono_grande = None
icono_chico = None


class FormularioCriminal(tk.Tk):
    """Formulario de registro de criminal"""

    def __init__(self,edit=False,persona_id=0,complice = False):
        super().__init__()
        self.edit = edit
        self.persona_id = persona_id
        self.complice = complice
        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Criminal')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/persona_entry.png'
        sig_file = './src/img/sig_button.png'
        back_file = './src/img/back_button.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)
        # sig_file = os.path.join(os.path.dirname(__file__), "sig_button.png")
        global ButtonImg
        ButtonImg = tk.PhotoImage(file=sig_file)
        # bg_file = os.path.join(os.path.dirname(__file__), "sig_button.png")
        global ButtonImg2
        ButtonImg2 = tk.PhotoImage(file=back_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        if self.edit:
            persona_data = get_persona(self.persona_id)

        dni_text = tk.StringVar()
        if self.edit:
            dni_text.set(persona_data[0][0])
        else:
            dni_text.set("")
        self.dni_entry = tk.Entry(self, background="#EFA11A", 
            font=("Cascadia Code Normal", 16), fg="white", textvariable= dni_text)
        if self.edit:
             self.dni_entry.config(bd=0, state='disabled')
        else:
            self.dni_entry.config(bd=0)
        self.dni_entry.place(x=234, y=250, height=31, width=210)
        self.dni_entry.lift()

        name_text = tk.StringVar()
        if self.edit:
            name_text.set(persona_data[0][1])
        else:
            name_text.set("")
        self.name_entry = tk.Entry(self, background="#EFA11A", 
            font=("Cascadia Code Normal", 16), fg="white", textvariable=name_text)
        self.name_entry.config(bd=0)
        self.name_entry.place(x=234, y=300, height=31, width=210)
        self.name_entry.lift()

        lastname_text = tk.StringVar()
        if self.edit:
            lastname_text.set(persona_data[0][2])
        else:
            lastname_text.set("")
        self.lastname_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code Normal", 16), fg="white", textvariable=lastname_text)
        self.lastname_entry.config(bd=0)
        self.lastname_entry.place(x=234, y=350, height=31, width=210)
        self.lastname_entry.lift()

        alias_text = tk.StringVar()
        if self.edit:
            alias_text.set(persona_data[0][8])
        else:
            alias_text.set("")
        self.alias_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code Normal", 16), fg="white", textvariable=alias_text)
        self.alias_entry.config(bd=0)
        self.alias_entry.place(x=234, y=400, height=31, width=210)
        self.alias_entry.lift()

        dob_text = tk.StringVar()
        if self.edit:
            dob_text.set(persona_data[0][3])
        else:
            dob_text.set("")
        self.dob_entry = tk.Entry(self, background="#EFA11A", font=(
            "Cascadia Code Normal", 16), fg="white", textvariable=dob_text)
        self.dob_entry.config(bd=0)
        self.dob_entry.place(x=234, y=580, height=31, width=210)
        self.dob_entry.lift()

        # telefono
        phone_text = tk.StringVar()
        if self.edit:
            phone_text.set(persona_data[0][5])
        else:
            phone_text.set("")
        self.phone_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code Normal", 16), fg="white", textvariable=phone_text)
        self.phone_entry.config(bd=0)
        self.phone_entry.place(x=646, y=450, height=31, width=305)
        self.phone_entry.lift()

        # direccion
        address_text = tk.StringVar()
        if self.edit:
            address_text.set(persona_data[0][6])
        else:
            address_text.set("")
        self.address_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code Normal", 16), fg="white", textvariable=address_text)
        self.address_entry.config(bd=0)
        self.address_entry.place(x=646, y=500, height=31, width=305)
        self.address_entry.lift()

        # """ NO TOCAR """

        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                          {'configure':
                                           {'selectbackground': '#EFA11A',  # Color al seleccionar una opcion
                                            'fieldbackground': '#EFA11A',  # Color del fondo
                                            'background': '#EFA11A',  # color de la flechita
                                            # tipo de fuente
                                            'font': ('Cascadia Code Normal', 16),
                                            'foreground': 'white',  # color de la fuente
                                            'borderwidth': '0',
                                            'highlightthickness': '0'  # borde
                                            }}}
                                )
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        combostyle.theme_use('combostyle')
        sex = ["Masculino", "Femenino"]
        self.sex_entry = ttk.Combobox(
            state="readonly",
            values=sex,
            font=("Cascadia Code Normal", 16),
        )
        if self.edit:
            sex_index = sex.index(persona_data[0][4])
            self.sex_entry.current(sex_index)
        else:
            self.sex_entry.current(0)
        self.sex_entry.place(x=234, y=500, height=31, width=210)
        self.sex_entry.pack
        # Nacionalidad NI SE TE OCURRA TOCAR.
        combostyle.theme_use('combostyle')
        nationalities = ['Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Brasil', 'Canadá',
                  'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'República Dominicana',
                  'Ecuador', 'El Salvador', 'Estados Unidos', 'España', 'Guatemala','Guyana', 
                  'Haití', 'Honduras', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 
                  'Perú', 'Puerto Rico', 'Saint Kitts y Nevis', 'Santa Lucía', 'San Vicente y las Granadinas', 
                  'Surinam', 'Trinidad y Tobago', 'Uruguay', 'Venezuela']
           
        self.nationality_entry = ttk.Combobox(
            state="readonly",
            values=nationalities,
            font=("Cascadia Code Normal", 16),
        )
        if self.edit:
            nationality_index = nationalities.index(persona_data[0][7])
            self.nationality_entry.current(nationality_index)
        else:
            self.nationality_entry.current(0)
        self.nationality_entry.current(0)
        self.nationality_entry.place(x=234, y=450, height=31, width=210)
        self.nationality_entry.pack

        self.btn_next = tk.Button(
            bd=0, image=ButtonImg, activebackground='black', command=self.save_data)
        self.btn_next.place(x=716, y=575, height=79, width=235)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg2, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

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
                'Documento inválido', 'El campo Documento debe tener mínimo 7 dígitos y máximo 10.')
            return

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

        alias = self.alias_entry.get().strip()

        if re.match(self.regex_alias, alias) is None:
            messagebox.showwarning(
                'Alias inválido', 'El campo Alias debe tener máximo 45 caracteres.')
            return

        fecha = self.dob_entry.get().strip()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'El campo Fecha de nacimiento debe cumplir con el formato YYYY-MM-DD (e.g., 2004-01-31).')
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
        
        self.datos_criminal = list(criminal_data.values())

        from pages.senas_identificacion import FormularioIdentificacion
        self.destroy()
        FormularioIdentificacion(self.datos_criminal,self.edit,self.persona_id)

    def clean(self):
        """Limpiar los campos del formulario"""
        self.dni_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.sex_entry.current(0)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.nationality_entry.current(0)
        self.alias_entry.delete(0, tk.END)
    
    def back_to_menu(self):
        """Volver al menu"""
        from pages.show_implicado import MostrarImplicados
        from pages.show_complice import MostrarComplice
        from main import MenuApp
        self.destroy()
        if self.complice:
            MostrarComplice()
        elif self.edit and self.complice == False:
            MostrarImplicados()
        else:        
            MenuApp()


def main():
    """Renderizar la aplicacion"""
    app = FormularioCriminal()
    app.mainloop()


if __name__ == '__main__':
    main()
