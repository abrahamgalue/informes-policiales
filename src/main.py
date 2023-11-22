"""Reseñas Policiales"""
import tkinter as tk
from pages.select_personas_arresto import PersonasArresto
from pages.exportar import ExportarDatos
from pages.show_arrestos import MostrarArrestos
from pages.criminal import FormularioCriminal
from pages.visualize import VisualizePersona
from pages.see_creditos import SeeCreditos
img = None
ButtonPersona1 = None
ButtonPersona2 = None
ButtonArresto = None
ButtonExportar = None
ButtonCreditos = None
icono_grande = None
icono_chico = None


class MenuApp(tk.Tk):
    """Menu de Reseñas Policiales"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Reseñas Policiales')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/main_menu.png'
        arresto_file = './src/img/main_btn/arresto_btn.png'
        persona1_file = './src/img/main_btn/persona1_btn.png'
        persona2_file = './src/img/main_btn/persona2_btn.png'
        exportar_file = './src/img/main_btn/exportar_btn.png'
        creditos_file = './src/img/main_btn/creditos_btn.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonPersona1
        ButtonPersona1 = tk.PhotoImage(file=persona1_file)

        global ButtonPersona2
        ButtonPersona2 = tk.PhotoImage(file=persona2_file)

        global ButtonArresto
        ButtonArresto = tk.PhotoImage(file=arresto_file)

        global ButtonExportar
        ButtonExportar = tk.PhotoImage(file=exportar_file)

        global ButtonCreditos
        ButtonCreditos = tk.PhotoImage(file=creditos_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        btn_registrar_persona = tk.Button(
            bd=0, image=ButtonPersona1, activebackground='#01080e', command=self.to_register_persona)
        btn_registrar_persona.place(x=115, y=410, height=79.7, width=235.9)

        btn_registrar_arresto = tk.Button(
            bd=0, image=ButtonArresto, activebackground='#01080e', command=self.to_register_arresto)
        btn_registrar_arresto.place(x=115, y=540, height=79.7, width=235.9)

        btn_exportar = tk.Button(
            bd=0, image=ButtonExportar, activebackground='#01080e', command=self.to_exportar)
        btn_exportar.place(x=382.5, y=477, height=79.7, width=235.9)

        self.btn_view_persona = tk.Button(
            bd=0, image=ButtonPersona2, activebackground='#01080e', command=self.to_vizualise)
        self.btn_view_persona.place(x=650, y=410, height=79.7, width=235.9)

        self.btn_view_arresto = tk.Button(
            bd=0, image=ButtonArresto, activebackground='#01080e', command=self.to_show_arrestos)
        self.btn_view_arresto.place(x=650, y=540, height=79.7, width=235.9)

        self.btn_creditos = tk.Button(
            bd=0, image=ButtonCreditos, activebackground='#01080e',command=self.to_credits)
        self.btn_creditos.place(x=417.9, y=656.7, height=55.5, width=164.3)
    
    def to_register_persona(self):
        """Create a new person"""
        self.destroy()
        FormularioCriminal()
        
    def to_register_arresto(self):
        """Create a new record"""
        self.destroy()
        PersonasArresto()

    def to_vizualise(self):
        """Mostrar tabla de arrestos"""
        self.destroy()
        VisualizePersona()
    
    def to_show_arrestos(self):
        """Mostrar tabla de arrestos"""
        self.destroy()
        MostrarArrestos()
        
    def to_exportar(self):
        """Exportar datos"""
        self.destroy()
        ExportarDatos()

    def to_credits(self):
        """ mostrar creditos """
        self.destroy()    
        SeeCreditos()
        
    def clean(self):
        """Limpiar los campos del formulario"""
        self.date_entry.delete(0, tk.END)
        self.judgment_entry.delete(0, tk.END)


def main():
    """Renderizar la aplicacion"""
    app = MenuApp()
    app.mainloop()


if __name__ == '__main__':
    main()
