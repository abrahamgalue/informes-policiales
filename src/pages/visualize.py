"""Ver persona"""
import tkinter as tk

img = None
ButtonImg = None
icono_grande = None
icono_chico = None
ButtonImplicados = None
ButtonComplices = None
ButtonTodas = None


class VisualizePersona(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/visualize.png'
        implicados_file = './src/img/visualize_btn/implicados_btn.png'
        complices_file= './src/img/visualize_btn/complices_btn.png'
        todas_file= './src/img/visualize_btn/todas_btn.png'
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

        global ButtonImplicados
        ButtonImplicados=tk.PhotoImage(file=implicados_file)

        global ButtonComplices
        ButtonComplices=tk.PhotoImage(file=complices_file)
        
        global ButtonTodas
        ButtonTodas=tk.PhotoImage(file=todas_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        self.btn_implicados= tk.Button(
            bd=0, image=ButtonImplicados, activebackground='#021118', command=self.to_implicado)
        self.btn_implicados.place(x=119.1, y=354.1, height=79.7, width=267.1)


        self.btn_complices= tk.Button(
            bd=0, image=ButtonComplices, activebackground='#021118', command=self.to_complices)
        self.btn_complices.place(x=650.7, y=354.1, height=79.7, width=267.1)
        
        self.btn_todas= tk.Button(
            bd=0, image=ButtonTodas, activebackground='#021118', command=self.to_todas)
        self.btn_todas.place(x=400, y=500, height=80, width=235.9)


        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)
        

    def back_to_menu(self):
        """Volver al menu"""
        from main import MenuApp
        self.destroy()
        MenuApp()
    def to_implicado(self):
        from pages.show_implicado import MostrarImplicados
        self.destroy()
        MostrarImplicados()
    def to_complices(self):
        from pages.show_complice import MostrarComplice
        self.destroy()
        MostrarComplice()
    def to_todas(self):
        from pages.show_persona import MostrarPersonas
        self.destroy()
        MostrarPersonas()

def main():
    """Renderizar la aplicacion"""
    app = VisualizePersona()
    app.mainloop()


if __name__ == '__main__':
    main()