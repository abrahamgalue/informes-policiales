"""Ver persona"""
import tkinter as tk
from tkinter import ttk

datos_arresto = []
img = None
ButtonImg = None
icono_grande = None
icono_chico = None
ButtonSig = None


class SeePersona(tk.Tk):
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
        sig_file = './src/img/see_persona_btn/senas_btn.png'
        back_file = './src/img/back_button.png'
        ver_file= './src/img/see_persona_btn/ver_btn.png'

        global icono_grande
        icono_grande = tk.PhotoImage(file='./src/img/icon-32.png')

        global icono_chico
        icono_chico = tk.PhotoImage(file='./src/img/icon-16.png')

        self.iconphoto(False, icono_grande, icono_chico)

        global img
        img = tk.PhotoImage(file=bg_file)

        global ButtonImg
        ButtonImg = tk.PhotoImage(file=back_file)

        global ButtonSig
        ButtonSig=tk.PhotoImage(file=sig_file)

        global ButtonVer
        ButtonVer=tk.PhotoImage(file=ver_file)

        self.fondo = tk.Canvas(self, width=1000, height=750)
        self.fondo.create_image(0, 0, image=img, anchor='nw')
        self.fondo.pack()

        self.btn_senas= tk.Button(
            bd=0, image=ButtonSig, activebackground='#021118')
        self.btn_senas.place(x=119.1, y=354.1, height=79.7, width=267.1)


        self.btn_senas= tk.Button(
            bd=0, image=ButtonSig, activebackground='#021118')
        self.btn_senas.place(x=650.7, y=354.1, height=79.7, width=267.1)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to_menu)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)
        

    def back_to_menu(self):
        """Volver al menu"""
        from main import MenuApp
        self.destroy()
        MenuApp()


def main():
    """Renderizar la aplicacion"""
    app = SeePersona()
    app.mainloop()


if __name__ == '__main__':
    main()