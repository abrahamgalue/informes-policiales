"""Ver arresto"""
import tkinter as tk
from tkinter import ttk

datos_arresto = []
img = None
ButtonImg = None
ButtonSig = None
icono_grande = None
icono_chico = None
ButtonVer=None


class SeeArresto(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        """Configurar la interfaz gráfica"""
        self.title('Exportar Datos')
        self.geometry("1000x750")
        self.resizable(0, 0)

        bg_file = './src/img/arresto_condena_see.png'
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

        f_text = tk.StringVar()
        f_text.set("31-01-2004")
        self.fecha_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=f_text,state='readonly')
        self.fecha_text.config(bd=0)
        self.fecha_text.place(x=232, y=185, height=31, width=210)
        self.fecha_text.lift()

        h_text = tk.StringVar()
        h_text.set("3:55")
        self.nombre_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=h_text,state='readonly')
        self.nombre_text.config(bd=0)
        self.nombre_text.place(x=232, y=235, height=31, width=210)
        self.nombre_text.lift()

        lu_text = tk.StringVar()
        lu_text.set("Sambil maracaibo")
        self.apellido_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=lu_text,state='readonly')
        self.apellido_text.config(bd=0)
        self.apellido_text.place(x=232, y=285, height=31, width=210)
        self.apellido_text.lift()


        des_text = tk.StringVar()
        des_text.set("Un negro de mrda entro a preguntar precios (racismo)")
        self.descripcion_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=des_text, state='readonly')
        self.descripcion_text.config(bd=0)
        self.descripcion_text.place(x=232, y=335, height=31, width=693)
        self.descripcion_text.lift()

        #esquina superior derecha
        del_text = tk.StringVar()
        del_text.set("Negro ")
        self.delito_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=del_text, state='readonly')
        self.delito_text.config(bd=0)
        self.delito_text.place(x=603.7, y=185, height=31, width=321.3)
        self.delito_text.lift()

        tipDel_text = tk.StringVar()
        tipDel_text.set("Racial")
        self.nacimiento_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=tipDel_text, state='readonly')
        self.nacimiento_text.config(bd=0)
        self.nacimiento_text.place(x=609.1, y=285, height=31, width=321.3)
        self.nacimiento_text.lift()

        #abajo
        im_text = tk.StringVar()
        im_text.set("Si")
        self.implicado_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=im_text, state='readonly')
        self.implicado_text.config(bd=0)
        self.implicado_text.place(x=420.7, y=395, height=31, width=210)
        self.implicado_text.lift()

        C_text = tk.StringVar()
        C_text.set("Su esposa")
        self.complice_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=C_text, state='readonly')
        self.complice_text.config(bd=0)
        self.complice_text.place(x=420.7, y=445, height=31, width=210)
        self.complice_text.lift()

        #Condena

        d_text = tk.StringVar()
        d_text.set("21-11-2023")
        self.fecha_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=d_text, state='readonly')
        self.fecha_text.config(bd=0)
        self.fecha_text.place(x=241.5, y=575, height=31, width=210)
        self.fecha_text.lift()

        s_text = tk.StringVar()
        s_text.set("Ser parte de los que llevan el carruaje de Brito pa ir pa uurbe")
        self.sentencia_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=s_text, state='readonly')
        self.sentencia_text.config(bd=0)
        self.sentencia_text.place(x=241.5, y=625, height=31, width=683.5)
        self.sentencia_text.lift()





        self.btn_verI= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118')
        self.btn_verI.place(x=641.4, y=395, height=31, width=139.8)

        self.btn_verC= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118')
        self.btn_verC.place(x=641.4, y=445, height=31, width=139.8)

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
    app = SeeArresto()
    app.mainloop()


if __name__ == '__main__':
    main()
