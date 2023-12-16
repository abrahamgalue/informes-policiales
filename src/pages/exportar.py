"""Exportar Datos"""
import tkinter as tk
from tkinter import messagebox
datos_arresto = []
img = None
ButtonImg = None
ButtonPersonas = None
ButtonArrestos = None
ButtonTodo = None
icono_grande = None
icono_chico = None


class ExportarDatos(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/export.png'
        arrestos_file = './src/img/export_btn/arrestos_btn.png'
        personas_file = './src/img/export_btn/personas_btn.png'
        # todo_file = './src/img/export_btn/todo_btn.png'
        back_file = './src/img/back_button.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonImg
        ButtonImg = tk.PhotoImage(file=back_file)

        global ButtonPersonas
        ButtonPersonas = tk.PhotoImage(file=personas_file)

        global ButtonArrestos
        ButtonArrestos = tk.PhotoImage(file=arrestos_file)

        # global ButtonTodo
        # ButtonTodo = tk.PhotoImage(file=todo_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        self.btn_export_personas = tk.Button(
            bd=0, image=ButtonPersonas, activebackground='#01060a',command=self.personas)
        self.btn_export_personas.place(x=366.5, y=300, height=79, width=267)

        self.btn_export_arrestos = tk.Button(
            bd=0, image=ButtonArrestos, activebackground='#01060a',command=self.arrestos)
        self.btn_export_arrestos.place(x=366.5, y=406.2, height=79, width=267)

        # self.btn_export_todo = tk.Button(
        #     bd=0, image=ButtonTodo, activebackground='#01060a')
        # self.btn_export_todo.place(x=366.5, y=512.3, height=79, width=267)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)

    def back_to_menu(self):
        """Volver al menu"""
        from main import MenuApp
        self.destroy()
        MenuApp()

    def personas(self):
        from pages.util.export import export_personas
        export_personas()
        messagebox.showinfo(
            'Mensaje', 'Los datos se exportaron de forma satisfactoria a la carpeta \informes-policiales\exports.')
    def arrestos(self):
        from pages.util.export import export_arrestos
        export_arrestos()
        messagebox.showinfo(
            'Mensaje', 'Los datos se exportaron de forma satisfactoria a la carpeta \informes-policiales\exports.')    

def main():
    """Renderizar la aplicacion"""
    app = ExportarDatos()
    app.mainloop()


if __name__ == '__main__':
    main()
