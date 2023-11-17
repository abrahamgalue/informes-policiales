"""Registro de Señas de Identificación"""
import re
import tkinter as tk
from tkinter import messagebox
from pages.criminal import tiene_complices,datos_criminal

datos_senas = []
img = None
ButtonImg = None
ButtonImg2 = None
icono_grande = None
icono_chico = None

class FormularioIdentificacion(tk.Tk):
    """Formulario de señas de identificacion"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Registro Señas Identificación')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/senas_entry.png'
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

        self.weight_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.weight_entry.config(bd=0)
        self.weight_entry.place(x=197.3, y=280, height=31, width=210)
        self.weight_entry.lift()

        self.height_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.height_entry.config(bd=0)
        self.height_entry.place(x=197.3, y=340, height=31, width=210)
        self.height_entry.lift()

        self.skin_color_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.skin_color_entry.config(bd=0)
        self.skin_color_entry.place(x=720, y=280, height=31, width=210)
        self.skin_color_entry.lift()

        self.hair_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.hair_entry.config(bd=0)
        self.hair_entry.place(x=197.3, y=400, height=31, width=210)
        self.hair_entry.lift()

        self.hair_color_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.hair_color_entry.config(bd=0)
        self.hair_color_entry.place(x=720, y=400, height=31, width=210)
        self.hair_color_entry.lift()

        self.eyes_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.eyes_entry.config(bd=0)
        self.eyes_entry.place(x=720, y=340, height=31, width=210)
        self.eyes_entry.lift()

        self.other_features_entry = tk.Entry(
            self, background="#EFA11A", font=("Cascadia Code", 16), fg="white")
        self.other_features_entry.config(bd=0)
        self.other_features_entry.place(x=364.6, y=460, height=31, width=565.4)
        self.eyes_entry.lift()

        self.btn_next = tk.Button(
            bd=0, image=ButtonImg, activebackground='black', command=self.save_data)
        self.btn_next.place(x=716, y=575, height=79, width=235)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg2, activebackground='#021118')
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

        # btn_limpiar = tk.Button(
        #     text='Limpiar', command=self.clean)
        # btn_limpiar.grid(row=8, column=3)

    def definir_patrones_validaciones(self):
        """Patrones de validación"""
        patron_peso = r'^[0-9]{2,3}\.[0-9]{2}$'
        self.regex_peso = re.compile(patron_peso)

        patron_altura = r'^[0-9]{2,3}\.[0-9]{2}$'
        self.regex_altura = re.compile(patron_altura)

        patron_color_piel = r'^.{3,45}$'
        self.regex_color_piel = re.compile(patron_color_piel)

        patron_cabello = r'^.{4,45}$'
        self.regex_cabello = re.compile(patron_cabello)

        patron_color_cabello = r'^.{5,45}$'
        self.regex_color_cabello = re.compile(patron_color_cabello)

        patron_ojos = r'^.{3,45}$'
        self.regex_ojos = re.compile(patron_ojos)

        patron_otras_caracteristicas = r'^.{0,60}$'
        self.regex_otras_caracteristicas = re.compile(
            patron_otras_caracteristicas)

    def save_data(self):
        """Create a dictionary"""

        peso = self.weight_entry.get().strip()

        if re.match(self.regex_peso, peso) is None:
            messagebox.showwarning(
                'Peso inválido', 'El campo Peso debe ser un número con mínimo 2 dígitos enteros y dos decimales (e.g., 93.14).')
            return

        altura = self.height_entry.get().strip()

        if re.match(self.regex_altura, altura) is None:
            messagebox.showwarning(
                'Altura inválida', 'El campo Altura debe ser un número con mínimo 2 dígitos enteros y dos decimales (e.g., 78.00).')
            return

        color_piel = self.skin_color_entry.get().strip()

        if re.match(self.regex_color_piel, color_piel) is None:
            messagebox.showwarning(
                'Color de piel inválido', 'El campo Color de piel debe tener mínimo 3 caracteres y máximo 45.')
            return

        cabello = self.hair_entry.get().strip()

        if re.match(self.regex_cabello, cabello) is None:
            messagebox.showwarning(
                'Cabello inválido', 'El campo Cabello debe tener mínimo 4 caracteres y máximo 45.')
            return

        color_cabello = self.hair_color_entry.get().strip()

        if re.match(self.regex_color_cabello, color_cabello) is None:
            messagebox.showwarning(
                'Color de cabello inválido', 'El campo Color de cabello debe tener mínimo 5 caracteres y máximo 45.')
            return

        ojos = self.eyes_entry.get().strip()

        if re.match(self.regex_ojos, ojos) is None:
            messagebox.showwarning(
                'Ojos inválidos', 'El Campo Ojos debe tener mínimo 3 caracteres y máximo 45.')
            return

        otras_caracteristicas = self.other_features_entry.get().strip()

        if re.match(self.regex_otras_caracteristicas, otras_caracteristicas) is None:
            messagebox.showwarning(
                'Otras caracteristicas inválidas', 'El campo Otras caracteristicas debe tener como máximo 60 caracteres.')
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
        print(tiene_complices)
        global datos_senas
        datos_senas = list(criminal_data.values())
        datos_senas.append(datos_criminal[0])
        print(datos_senas)
        
        messagebox.showinfo(
            'Mensaje', 'Los datos se guardaron de forma satisfactoria.')
        from pages.condena import FormularioCondena
        from pages.complices import FormularioComplices
        self.destroy()

        if tiene_complices:
            FormularioComplices()
        else:
            FormularioCondena()

    def clean(self):
        """Limpiar los campos del formulario"""
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.skin_color_entry.delete(0, tk.END)
        self.hair_entry.delete(0, tk.END)
        self.hair_color_entry.delete(0, tk.END)
        self.eyes_entry.delete(0, tk.END)
        self.other_features_entry.delete(0, tk.END)


def main():
    """Renderizar la aplicacion"""
    app = FormularioIdentificacion()
    app.mainloop()


if __name__ == '__main__':
    main()
