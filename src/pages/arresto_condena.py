"""Registro de Arresto y Condena"""
import re
import tkinter as tk
from tkinter import messagebox

datos_arresto = []

img = None
ButtonImg = None
ButtonImg2 = None
icono_grande = None
icono_chico = None

class FormularioArresto(tk.Tk):
    """Formulario de registro de arresto y condena"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Arresto y Condena')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/arresto_condena_entry.png'
        sig_file = './src/img/sig_button.png'
        back_file = './src/img/back_button.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonImg
        ButtonImg = tk.PhotoImage(file=sig_file)

        global ButtonImg2
        ButtonImg2 = tk.PhotoImage(file=back_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        self.arrest_date_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.arrest_date_entry.config(bd=0)
        self.arrest_date_entry.place(x=234, y=183, height=31, width=210)
        self.arrest_date_entry.lift()

        self.hour_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.hour_entry.config(bd=0)
        self.hour_entry.place(x=234, y=233, height=31, width=210)
        self.hour_entry.lift()

        self.place_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.place_entry.config(bd=0)
        self.place_entry.place(x=234, y=283, height=31, width=210)
        self.place_entry.lift()

        self.crime_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.crime_entry.config(bd=0)
        self.crime_entry.place(x=715, y=183, height=31, width=210)
        self.crime_entry.lift()

        self.type_of_crime_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.type_of_crime_entry.config(bd=0)
        self.type_of_crime_entry.place(x=715, y=233, height=31, width=210)
        self.type_of_crime_entry.lift()

        self.description_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.description_entry.config(bd=0)
        self.description_entry.place(x=715, y=283, height=31, width=210)
        self.description_entry.lift()

        self.date_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.date_entry.config(bd=0)
        self.date_entry.place(x=234, y=478, height=31, width=210)
        self.date_entry.lift()

        self.judgment_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.judgment_entry.config(bd=0)
        self.judgment_entry.place(x=715, y=478, height=31, width=210)
        self.judgment_entry.lift()

        self.btn_next = tk.Button(
            bd=0, image=ButtonImg, activebackground='black', command=self.save_data)
        self.btn_next.place(x=716, y=575, height=79, width=235)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg2, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

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

        patron_sentencia = r'^.{1,128}$'
        self.regex_sentencia = re.compile(patron_sentencia)

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

        fecha = self.date_entry.get().strip()

        if re.match(self.regex_fecha, fecha) is None:
            messagebox.showwarning(
                'Fecha inválida', 'El campo Fecha debe cumplir con el formato YYYY-MM-DD (e.g., 2004-11-24).')
            return

        sentencia = self.judgment_entry.get().strip()

        if re.match(self.regex_sentencia, sentencia) is None:
            messagebox.showwarning(
                'Sentencia inválida', 'El campo sentencia es obligatorio y debe tener máximo 128 caracteres.')
            return

        criminal_data = {
            "Fecha": self.date_entry.get(),
            "Sentencia": self.judgment_entry.get()
        }

        print(criminal_data)
        
        global datos_arresto
        datos_arresto = list(criminal_data.values())
       
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
    
    def back_to_menu(self):
        """Volver al menu"""
        from main import MenuApp
        self.destroy()
        MenuApp()


def main():
    """Renderizar la aplicacion"""
    app = FormularioArresto()
    app.mainloop()


if __name__ == '__main__':
    main()
