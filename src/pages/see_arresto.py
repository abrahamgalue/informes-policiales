"""Ver arresto"""
import tkinter as tk
from tkinter import ttk
from pages.util.ocurrencia_de_arresto import get_arresto
from pages.util.cond import get_condena
from pages.util.persona import get_complices_arresto

img = None
ButtonImg = None
ButtonSig = None
icono_grande = None
icono_chico = None
ButtonVer=None


class SeeArresto(tk.Tk):
    """Página de exportación de datos"""

    def __init__(self, arresto_id,persona=False,complice=False, persona_id = 0):
        super().__init__()
        self.arresto_id = arresto_id
        self.persona = persona
        self.persona_id = persona_id
        self.complice = complice
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

        self.arresto_data = get_arresto(self.arresto_id)
        condena_data = get_condena(self.arresto_id)
        
        f_text = tk.StringVar()
        f_text.set(self.arresto_data[0][1])
        self.fecha_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=f_text,state='readonly')
        self.fecha_text.config(bd=0)
        self.fecha_text.place(x=232, y=185, height=31, width=210)
        self.fecha_text.lift()

        h_text = tk.StringVar()
        h_text.set(self.arresto_data[0][2])
        self.nombre_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=h_text,state='readonly')
        self.nombre_text.config(bd=0)
        self.nombre_text.place(x=232, y=235, height=31, width=210)
        self.nombre_text.lift()

        lu_text = tk.StringVar()
        lu_text.set(self.arresto_data[0][3])
        self.apellido_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=lu_text,state='readonly')
        self.apellido_text.config(bd=0)
        self.apellido_text.place(x=232, y=285, height=31, width=210)
        self.apellido_text.lift()


        des_text = tk.StringVar()
        des_text.set(self.arresto_data[0][6])
        self.descripcion_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=des_text, state='readonly')
        self.descripcion_text.config(bd=0)
        self.descripcion_text.place(x=232, y=335, height=31, width=693)
        self.descripcion_text.lift()

        #esquina superior derecha
        del_text = tk.StringVar()
        del_text.set(self.arresto_data[0][4])
        self.delito_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=del_text, state='readonly')
        self.delito_text.config(bd=0)
        self.delito_text.place(x=603.7, y=185, height=31, width=321.3)
        self.delito_text.lift()

        tipDel_text = tk.StringVar()
        tipDel_text.set(self.arresto_data[0][5])
        self.nacimiento_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=tipDel_text, state='readonly')
        self.nacimiento_text.config(bd=0)
        self.nacimiento_text.place(x=609.1, y=285, height=31, width=321.3)
        self.nacimiento_text.lift()

        #implicado
        im_text = tk.StringVar()
        im_text.set(self.arresto_data[0][7])
        self.implicado_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=im_text, state='readonly')
        self.implicado_text.config(bd=0)
        self.implicado_text.place(x=420.7, y=395, height=31, width=210)
        self.implicado_text.lift()

        self.combostyle = ttk.Style()

        self.combostyle.theme_create('combostyle', parent='alt',
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
        self.combostyle.theme_use('combostyle')
        complices = list()
        complices_data = get_complices_arresto(self.arresto_id)
        if complices_data == []:
            complices = ["No hay"]
        else:   
            for i in range(len(complices_data)):
                complices.append(complices_data[i][0])
        self.complice_entry = ttk.Combobox(
            state="readonly",
            values=complices,
            font=("Cascadia Code Normal", 16),
        )
        self.complice_entry.current(0)
        self.complice_entry.place(x=420.7, y=445, height=31, width=210)
        self.complice_entry.pack
        
        """ C_text = tk.StringVar()
        C_text.set("Su esposa")
        self.complice_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=C_text, state='readonly')
        self.complice_text.config(bd=0)
        self.complice_text.place(x=420.7, y=445, height=31, width=210)
        self.complice_text.lift() """

        #Condena

        d_text = tk.StringVar()
        d_text.set(condena_data[0][0])
        self.fecha_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=d_text, state='readonly')
        self.fecha_text.config(bd=0)
        self.fecha_text.place(x=241.5, y=575, height=31, width=210)
        self.fecha_text.lift()

        s_text = tk.StringVar()
        s_text.set(condena_data[0][1])
        self.sentencia_text = tk.Entry(
            self,background="white", font=("Cascadia Code Normal", 16), fg="#EFA11A",textvariable=s_text, state='readonly')
        self.sentencia_text.config(bd=0)
        self.sentencia_text.place(x=241.5, y=625, height=31, width=683.5)
        self.sentencia_text.lift()





        self.btn_verI= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118',command=self.see_implicado)
        self.btn_verI.place(x=641.4, y=395, height=31, width=139.8)

        self.btn_verC= tk.Button(
            bd=0, image=ButtonVer, activebackground='#021118',command=self.see_complice)
        self.btn_verC.place(x=641.4, y=445, height=31, width=139.8)

        self.btn_back = tk.Button(
            bd=0, image=ButtonImg, activebackground='#021118', command=self.back_to)
        self.btn_back.place(x=75, y=87.3, height=53, width=95)
        
 

    def back_to(self):
        """Volver al menu"""
        if self.persona:
            from pages.see_persona import SeePersona
            self.destroy()
            SeePersona(persona_id=self.persona_id, complice=self.complice)
        else:
            from pages.show_arrestos import MostrarArrestos
            self.destroy()
            MostrarArrestos()
        
    def see_implicado(self):        
        from pages.see_persona import SeePersona    
        implicado_id = self.arresto_data[0][7]
        self.destroy()
        SeePersona(persona_id=implicado_id,arresto=True,arresto_id=self.arresto_id)
    
    def see_complice(self):        
        from pages.see_persona import SeePersona
        complice_id = str(self.complice_entry.get())
        if complice_id == "No hay":
            print("No hay")
        else:
            self.destroy()
            SeePersona(persona_id=complice_id,arresto=True,arresto_id=self.arresto_id, complice=True)

            
        

def main():
    """Renderizar la aplicacion"""
    app = SeeArresto()
    app.mainloop()


if __name__ == '__main__':
    main()
